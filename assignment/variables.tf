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
variable "code_repo" {
  description = "Repository of application code"
  type        = string
}
variable "app_port" {
  description = "Exposed container port"
  type        = string
}
variable "vpc_cidr" {
  description = "CIDR for main VPC"
  type        = string
}
variable "newbits" {
  description = "Newbits value for dynamic subnet creation"
  type        = string
}
