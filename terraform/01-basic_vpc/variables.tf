variable "ingress_ports" {
  description = "List of ports for ingress rules"
  type        = list(number)
  default     = [22, 80, 443]
}
variable "aws_region" {
  description = "AWS region for all resources"
  type        = string
  default     = "eu-north-1"
}
