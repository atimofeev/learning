variable "project" {
  description = "Project name"
  type        = string
}
variable "env" {
  description = "Environment"
  type        = string
}
variable "vpc_id" {
  description = "ID of main VPC"
  type        = string
}
variable "public_subnet_ids" {
  description = "List of public subnet IDs"
  type        = list(any)
}
variable "alb_sg" {
  description = "List of ALB Security Groups"
  type        = string
}
