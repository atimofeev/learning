# ----- VPC ----- #
resource "aws_vpc" "vpc_main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = {
    Name               = "Main ${upper(var.env)} VPC"
  }
}

# ----- Subnets ----- #
data "aws_availability_zones" "available" {}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, var.newbits, count.index)
  availability_zone = element(data.aws_availability_zones.available.names, count.index)
  tags              = {
    Name            = "${var.project}-${var.env}-public-sn-${count.index}"
  }
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, var.newbits, count.index + 2)
  availability_zone = element(data.aws_availability_zones.available.names, count.index)
  tags              = {
    Name            = "${var.project}-${var.env}-private-sn-${count.index}"
  }
}

# ----- Internet Gateway ----- #
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc_main.id
  tags   = {
    Name = "${var.project}-${var.env}-igw"
  }
}

# ----- Routing ----- #
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.vpc_main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags   = {
    Name = "${var.project}-${var.env}-public-rt"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.vpc_main.id
  tags   = {
    Name = "${var.project}-${var.env}-private-rt"
  }
}

resource "aws_route_table_association" "public" {
  count          = length(aws_subnet.public.*.id)
  subnet_id      = element(aws_subnet.public.*.id, count.index)
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count          = length(aws_subnet.private.*.id)
  subnet_id      = element(aws_subnet.private.*.id, count.index)
  route_table_id = aws_route_table.private.id
}

# ----- Security Groups ----- #
resource "aws_security_group" "alb" {
  name        = "alb-sg"
  description = "ALB default security group"
  vpc_id      = aws_vpc.vpc_main.id
  ingress {
    protocol    = "TCP"
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ecs_tasks" {
  name        = "ecs-tasks-sg"
  description = "allow inbound access from the ALB only"
  vpc_id      = aws_vpc.vpc_main.id
  ingress {
    protocol        = "TCP"
    from_port       = var.app_port
    to_port         = var.app_port
    cidr_blocks     = ["0.0.0.0/0"]
    security_groups = [aws_security_group.alb.id]
  }
  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ----- Endpoints ----- #
resource "aws_vpc_endpoint" "ecr_api" {
  vpc_id             = aws_vpc.vpc_main.id
  service_name       = "com.amazonaws.${var.region}.ecr.api"
  vpc_endpoint_type  = "Interface"
  security_group_ids = [aws_security_group.ecs_tasks.id]
  subnet_ids         = aws_subnet.private[*].id
}

resource "aws_vpc_endpoint" "ecr_dkr" {
  vpc_id             = aws_vpc.vpc_main.id
  service_name       = "com.amazonaws.${var.region}.ecr.dkr"
  vpc_endpoint_type  = "Interface"
  security_group_ids = [aws_security_group.ecs_tasks.id]
  subnet_ids         = aws_subnet.private[*].id
}
