output "vpc_id" {
  value = aws_vpc.vpc_main.id
}
output "public_subnet_ids" {
  value = aws_subnet.public.*.id
}
output "private_subnet_ids" {
  value = aws_subnet.private.*.id
}
output "alb_sg" {
  value = aws_security_group.alb.id
}
output "ecs_sg" {
  value = aws_security_group.ecs_tasks.id
}
