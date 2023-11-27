data "aws_caller_identity" "current" {}

data "aws_iam_policy_document" "ecs_tasks" {
  statement {
    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:ListBucket"
    ]
    resources = [
      "arn:aws:s3:::${var.image_storage_bucket}",
      "arn:aws:s3:::${var.image_storage_bucket}/*"
    ]
  }

  statement {
    actions =[
      "kms:Decrypt",
      "kms:Encrypt",
      "kms:ReEncrypt*",
      "kms:GenerateDataKey*",
      "kms:DescribeKey"
    ]
    resources = [
      "${var.image_storage_kms_key_arn}"
    ]
  }

  statement {
    actions = [
      "ecr:GetAuthorizationToken",
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["*"]
  }
  statement {
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]
    resources = [
      "arn:aws:logs:${var.region}:${data.aws_caller_identity.current.account_id}:log-group:${var.project}-${var.env}:*"
    ]
  }
}

data "aws_iam_policy_document" "ecs_tasks_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_policy" "ecs_tasks" {
  name               = "${var.project}-${var.env}-ecs-tasks-execution"
  policy             = data.aws_iam_policy_document.ecs_tasks.json
}

resource "aws_iam_role" "ecs_tasks" {
  name               = "${var.project}-${var.env}-ecs-tasks-execution"
  assume_role_policy = data.aws_iam_policy_document.ecs_tasks_assume_role.json
}

resource "aws_iam_role_policy_attachment" "ecs_tasks" {
  role               = aws_iam_role.ecs_tasks.name
  policy_arn         = aws_iam_policy.ecs_tasks.arn
}
