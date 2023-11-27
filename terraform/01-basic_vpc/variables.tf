variable "ingress_ports" {
  description = "List of ports for ingress rules"
  type        = list(number)
  default     = [22, 80, 443]
}
