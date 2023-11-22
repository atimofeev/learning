output "build_artifacts_bucket" {
  value = aws_s3_bucket.build_artifacts.bucket
}
output "image_storage_bucket" {
  value = aws_s3_bucket.image_storage.bucket
}
output "image_storage_kms_key_arn" {
  value = aws_kms_key.image_storage.arn
}
