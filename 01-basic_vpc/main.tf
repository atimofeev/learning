# Basic VPC with 2xEC2 - 1xPublic, 1xPrivate
# Public EC2 hosts Hello World! message via HTTP
# credentials are provided with ~/.aws/credentials
terraform {
  required_providers {
    aws = {
      source  = "registry.terraform.io/hashicorp/aws"
      version = "5.13.1"
    }
    http = {
      source  = "registry.terraform.io/hashicorp/http"
      version = "3.4.0"
    }
  }
  required_version = "1.5.4"
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_vpc" "test_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "test_vpc"
  }
}

resource "aws_internet_gateway" "test_public_gw" {
  vpc_id = aws_vpc.test_vpc.id
  tags = {
    Name = "test_public_gw"
  }
}

resource "aws_route_table" "test_public_rt" {
  vpc_id = aws_vpc.test_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.test_public_gw.id
  }
  tags = {
    Name = "test_public_rt"
  }
}

resource "aws_subnet" "test_public_sn_a" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-north-1a"
  tags = {
    Name = "test_public_sn_a"
  }
}

resource "aws_subnet" "test_private_sn_b" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "eu-north-1b"
  tags = {
    Name = "test_private_sn_b"
  }
}

resource "aws_route_table_association" "test_public_rt_ass" {
  subnet_id = aws_subnet.test_public_sn_a.id
  route_table_id = aws_route_table.test_public_rt.id
}

data "http" "myip" {
  url = "http://ipv4.icanhazip.com"
}

resource "aws_security_group" "test_public_sg" {
  name = "allow web traffic"
  vpc_id = aws_vpc.test_vpc.id

  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["${chomp(data.http.myip.response_body)}/32", "10.0.0.0/16"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "test_public_sg"
  }
}

resource "aws_security_group" "test_private_sg" {
  name = "allow local ssh"
  vpc_id = aws_vpc.test_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "test_private_sg"
  }
}

resource "aws_network_interface" "test_public_ni" {
  subnet_id = aws_subnet.test_public_sn_a.id
  private_ips = ["10.0.1.50"]
  security_groups = [ aws_security_group.test_public_sg.id ]
  tags = {
    Name = "test_public_ni"
  }
}

resource "aws_network_interface" "test_private_ni" {
  subnet_id = aws_subnet.test_private_sn_b.id
  private_ips = ["10.0.2.25"]
  security_groups = [ aws_security_group.test_private_sg.id ]
  tags = {
    Name = "test_private_ni"
  }
}

resource "aws_eip" "test_public_ip_address" {
  domain = "vpc"
  network_interface = aws_network_interface.test_public_ni.id
  associate_with_private_ip = aws_network_interface.test_public_ni.private_ip
  depends_on = [ aws_internet_gateway.test_public_gw ]
  tags = {
    Name = "test_public_ip_address"
  }
}

resource "aws_key_pair" "test_public_key" {
  key_name   = "test_public_key"
  public_key = file("~/.ssh/test_public_key.pub")
}

resource "aws_key_pair" "test_private_key" {
  key_name   = "test_private_key"
  public_key = file("~/.ssh/test_private_key.pub")
}

data "aws_key_pair" "private_key" {
  key_name   = "private_key"
}

resource "aws_instance" "test_public_instance" {
  ami           = "ami-04e4606740c9c9381"
  instance_type = "t3.micro"
  availability_zone = "eu-north-1a"
  key_name = aws_key_pair.test_public_key.key_name

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.test_public_ni.id
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo dnf update -y
              sudo dnf install nginx -y
              sudo mkdir -p /usr/share/nginx/html
              echo "Hello, World!" | sudo tee /usr/share/nginx/html/index.html
              sudo systemctl enable nginx
              sudo systemctl start nginx
              EOF

  tags = {
    Name = "test_public_instance"
    test_tag = "test_tag_value"
  }
}

resource "aws_instance" "test_private_instance" {
  ami           = "ami-04e4606740c9c9381"
  instance_type = "t3.micro"
  availability_zone = "eu-north-1b"
  key_name = data.aws_key_pair.private_key.key_name

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.test_private_ni.id
  }

  tags = {
    Name = "test_private_instance"
    test_tag = "test_tag_value2"
  }
}
