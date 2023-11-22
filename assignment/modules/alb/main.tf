resource "aws_lb" "front_end" {
  name                       = "${var.project}-${var.env}-alb"
  internal                   = false
  load_balancer_type         = "application"
  security_groups            = [var.alb_sg]
  subnets                    = var.public_subnet_ids
  enable_deletion_protection = false
}

# ----- Listeners ----- #
resource "aws_lb_listener" "http" {
  load_balancer_arn  = aws_lb.front_end.arn
  port               = "80"
  protocol           = "HTTP"
  default_action {
    type             = "fixed-response"
    fixed_response {
      content_type   = "text/plain"
      message_body   = "Fixed response content"
      status_code    = "200"
    }
  }
}

resource "aws_lb_listener_rule" "flask" {
  listener_arn       = aws_lb_listener.http.arn
  priority           = 100
  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.flask.arn
  }
  condition {
    path_pattern {
      values = ["/*"]
    }
  }
}

# ----- Target groups ----- #
resource "aws_lb_target_group" "flask" {
  name        = "${var.project}-${var.env}-tg-flask"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = var.vpc_id
  stickiness {
    type    = "lb_cookie"
    enabled = true
  }
  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = "2"
    port                = "80"
    path                = "/"
    protocol            = "HTTP"
    interval            = 5
    matcher             = "200,301,302"
  }
}
