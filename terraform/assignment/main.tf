provider "aws" {
  region = var.region
}

module "network" {
  source   = "./modules/network"
  project  = var.project
  env      = var.env
  region   = var.region
  app_port = var.app_port
  vpc_cidr = var.vpc_cidr
  newbits  = var.newbits
}

module "alb" {
  source            = "./modules/alb"
  project           = var.project
  env               = var.env
  vpc_id            = module.network.vpc_id
  public_subnet_ids = module.network.public_subnet_ids
  alb_sg            = module.network.alb_sg
}

module "iam" {
  source                    = "./modules/iam"
  project                   = var.project
  env                       = var.env
  region                    = var.region
  image_storage_bucket      = module.s3.image_storage_bucket
  image_storage_kms_key_arn = module.s3.image_storage_kms_key_arn
}

module "ecr" {
  source  = "./modules/ecr"
  project = var.project
  env     = var.env
}

module "codebuild" {
  source                 = "./modules/codebuild"
  project                = var.project
  env                    = var.env
  code_repo              = var.code_repo
  service_role           = module.iam.role_codebuild
  build_artifacts_bucket = module.s3.build_artifacts_bucket
  repository_url         = module.ecr.repository_url
}

module "ecs" {
  source               = "./modules/ecs"
  project              = var.project
  env                  = var.env
  region               = var.region
  app_port             = var.app_port
  private_subnet_ids   = module.network.private_subnet_ids
  ecs_sg               = module.network.ecs_sg
  role_ecs_tasks       = module.iam.role_ecs_tasks
  ecr_repo_url         = module.ecr.repository_url
  alb_tg               = module.alb.alb_tg
  image_storage_bucket = module.s3.image_storage_bucket
}

module "s3" {
  source  = "./modules/s3"
  project = var.project
  env     = var.env
}
