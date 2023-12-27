terraform {
  backend "s3" {
    bucket  = "tfstate-80f05283"
    encrypt = true
    key     = "terraform.tfstate"
    region  = "eu-north-1"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.26.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.5.1"
    }
  }
  required_version = "1.6.4"
}
