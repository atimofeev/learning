resource "random_string" "bucket" {
  length  = 7
  special = false
  upper   = false
  lower   = true
  numeric = true
  keepers = {
    env = var.env
  }
}

resource "aws_kms_key" "image_storage" {
  description = "Key for main image storage bucket"
}

resource "aws_s3_bucket" "image_storage" {
  bucket = "${var.project}-${var.env}-image-storage-${random_string.bucket.result}"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "image_storage" {
  bucket = aws_s3_bucket.image_storage.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = aws_kms_key.image_storage.arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_s3_bucket" "build_artifacts" {
  bucket = "${var.project}-${var.env}-artifacts-${random_string.bucket.result}"
}
