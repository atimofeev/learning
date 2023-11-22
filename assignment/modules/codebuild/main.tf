resource "aws_codebuild_project" "codebuild" {
  name = "${var.project}-${var.env}"
  service_role = var.service_role

  artifacts {
    type = "S3"
    location = var.build_artifacts_bucket
  }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image = "aws/codebuild/standard:4.0"
    type = "LINUX_CONTAINER"
    environment_variable {
      name = "REPO_URL"
      value = var.repository_url
    }
  }

  source {
    type = "GITHUB"
    location = var.code_repo
  }
}
