output "alb_arn" {
  value = aws_lb.front_end.arn
}
output "alb_tg" {
  value = aws_lb_target_group.flask.arn
}
