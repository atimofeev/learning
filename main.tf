# test platform configuration
# credentials are provided with ~/.aws/credentials
provider "aws" {
  region = "eu-north-1"
}

resource "aws_vpc" "test-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "test-vpc"
  }
}

resource "aws_internet_gateway" "test-gateway" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-gateway"
  }
}

resource "aws_route_table" "test-route-table" {
  vpc_id = aws_vpc.test-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.test-gateway.id
  }
  tags = {
    Name = "test-route-table"
  }
}

resource "aws_subnet" "test-subnet1" {
  vpc_id = aws_vpc.test-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-north-1a"
  tags = {
    Name = "test-subnet1"
  }
}

resource "aws_route_table_association" "test-rt-ass" {
  subnet_id = aws_subnet.test-subnet1.id
  route_table_id = aws_route_table.test-route-table.id
}

variable "ingress_ports" {
  description = "List of ports for ingress rules"
  type        = list(number)
  default     = [22, 80, 443]
}

resource "aws_security_group" "test-allow-web-sec-group" {
  name = "allow web traffic"
  vpc_id = aws_vpc.test-vpc.id

  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "test-allow-web-sec-group"
  }
}

resource "aws_network_interface" "test-webserver-network-interface" {
  subnet_id = aws_subnet.test-subnet1.id
  private_ips = ["10.0.1.50"]
  security_groups = [ aws_security_group.test-allow-web-sec-group.id ]
}

resource "aws_eip" "test-public-ip-address" {
  domain = "vpc"
  network_interface = aws_network_interface.test-webserver-network-interface.id
  associate_with_private_ip = aws_network_interface.test-webserver-network-interface.private_ip
  depends_on = [ aws_internet_gateway.test-gateway ]
}

resource "aws_instance" "test-instance" {
  ami           = "ami-04e4606740c9c9381"
  instance_type = "t3.micro"
  availability_zone = "eu-north-1a"
  #key_name = "test-key"

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.test-webserver-network-interface.id
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo dnf update -y
              sudo dnf install nginx -y
              sudo mkdir -p /var/www/html
              echo "Hello, World!" | sudo tee /var/www/html/index.html
              sudo systemctl enable nginx
              sudo systemctl start nginx
              EOF

  tags = {
    Name = "test-webserver-instance"
    test_tag = "test_tag_value"
  }
}