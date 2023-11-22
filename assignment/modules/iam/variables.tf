variable "project" {
  description = "Project name"
  type        = string
}
variable "env" {
  description = "Environment"
  type        = string
}
variable "region" {
  description = "Region"
  type        = string
}
variable "image_storage_bucket" {
  description = "Main image storage bucket name"
  type        = string
}
variable "image_storage_kms_key_arn" {
  description = "Access key to encrypted bucket"
  type        = string
}
