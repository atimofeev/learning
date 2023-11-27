variable "project" {
  description = "Project name"
  type        = string
}
variable "env" {
  description = "Environment"
  type        = string
}
variable "region" {
  description = "AWS region for all resources"
  type        = string
}
variable "app_port" {
  description = "Exposed container port"
  type        = string
}
variable "private_subnet_ids" {
  description = "List of private subnet IDs"
}
variable "ecs_sg" {
  description = "Security Group ID for ECS tasks"
  type        = string
}
variable "role_ecs_tasks" {
  description = "ECS tasks role"
  type        = string
}
variable "ecr_repo_url" {
  description = "ECR repository URL"
  type        = string
}
variable "alb_tg" {
  description = "ALB target group ARN"
  type        = string
}
variable "image_storage_bucket" {
  description = "Main storage bucket name"
  type        = string
}
