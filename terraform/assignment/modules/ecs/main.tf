resource "aws_ecs_cluster" "flask" {
  name = "${var.project}-${var.env}-cluster"
}

resource "aws_ecs_task_definition" "flask" {
  family                   = "${var.project}-${var.env}-task-family"
  network_mode             = "awsvpc"
  execution_role_arn       = var.role_ecs_tasks
  cpu                      = 256
  memory                   = 2048
  requires_compatibilities = ["FARGATE"]
  container_definitions = jsonencode([
    {
      "name" : "${var.project}-${var.env}-app",
      "image" : "${var.ecr_repo_url}:latest",
      "portMappings" : [
        {
          "containerPort" : tonumber(var.app_port),
          "hostPort" : tonumber(var.app_port),
          "protocol" : "tcp"
        }
      ],
      "logConfiguration" : {
        "logDriver" : "awslogs",
        "options" : {
          "awslogs-region" : "${var.region}",
          "awslogs-stream-prefix" : "${var.project}-${var.env}-service",
          "awslogs-group" : "${var.project}-${var.env}-log-group"
        }
      }
      "environment" : [
        {
          "name" : "BUCKET_NAME",
          "value" : "${var.image_storage_bucket}"
        },
      ],
      "essential" : true
    }
  ])
}

resource "aws_ecs_service" "flask" {
  name            = "${var.project}-${var.env}-service"
  cluster         = aws_ecs_cluster.flask.id
  task_definition = aws_ecs_task_definition.flask.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    security_groups = [var.ecs_sg]
    subnets         = var.private_subnet_ids
    #assign_public_ip = true
  }
  load_balancer {
    target_group_arn = var.alb_tg
    container_name   = "${var.project}-${var.env}-app"
    container_port   = var.app_port
  }
}

resource "aws_cloudwatch_log_group" "flask" {
  name = "${var.project}-${var.env}-log-group"
}
