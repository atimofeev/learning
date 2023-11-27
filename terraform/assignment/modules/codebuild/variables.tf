variable "project" {
  description = "Project name"
  type        = string
}
variable "env" {
  description = "Environment"
  type        = string
}
variable "code_repo" {
  description = "Repository of application code"
  type        = string
}
variable "service_role" {
  description = "Service role ARN which provides access to needed functionality"
  type        = string
}
variable "build_artifacts_bucket" {
  description = "S3 bucket to store build artifacts"
  type        = string
}
variable "repository_url" {
  description = "ECR repository URL where to put built image"
  type        = string
}
