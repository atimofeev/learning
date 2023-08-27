# Basic VPC with 2xEC2 - 1xPublic, 1xPrivate
# Public EC2 hosts Hello World! message via HTTP
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

resource "aws_internet_gateway" "test-public-gw" {
  vpc_id = aws_vpc.test-vpc.id
  tags = {
    Name = "test-public-gw"
  }
}

resource "aws_route_table" "test-public-rt" {
  vpc_id = aws_vpc.test-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.test-public-gw.id
  }
  tags = {
    Name = "test-public-rt"
  }
}

resource "aws_subnet" "test-public-sn-a" {
  vpc_id = aws_vpc.test-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-north-1a"
  tags = {
    Name = "test-public-sn-a"
  }
}

resource "aws_subnet" "test-private-sn-b" {
  vpc_id = aws_vpc.test-vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "eu-north-1b"
  tags = {
    Name = "test-private-sn-b"
  }
}

resource "aws_route_table_association" "test-public-rt-ass" {
  subnet_id = aws_subnet.test-public-sn-a.id
  route_table_id = aws_route_table.test-public-rt.id
}

variable "ingress_ports" {
  description = "List of ports for ingress rules"
  type        = list(number)
  default     = [22, 80, 443]
}

data "http" "myip" {
url = "http://ipv4.icanhazip.com"
}

resource "aws_security_group" "test-public-sg" {
  name = "allow web traffic"
  vpc_id = aws_vpc.test-vpc.id

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
    Name = "test-public-sg"
  }
}

resource "aws_security_group" "test-private-sg" {
  name = "allow local ssh"
  vpc_id = aws_vpc.test-vpc.id

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
    Name = "test-private-sg"
  }
}

resource "aws_network_interface" "test-public-ni" {
  subnet_id = aws_subnet.test-public-sn-a.id
  private_ips = ["10.0.1.50"]
  security_groups = [ aws_security_group.test-public-sg.id ]
  tags = {
    Name = "test-public-ni"
  }
}

resource "aws_network_interface" "test-private-ni" {
  subnet_id = aws_subnet.test-private-sn-b.id
  private_ips = ["10.0.2.25"]
  security_groups = [ aws_security_group.test-private-sg.id ]
  tags = {
    Name = "test-private-ni"
  }
}

resource "aws_eip" "test-public-ip-address" {
  domain = "vpc"
  network_interface = aws_network_interface.test-public-ni.id
  associate_with_private_ip = aws_network_interface.test-public-ni.private_ip
  depends_on = [ aws_internet_gateway.test-public-gw ]
  tags = {
    Name = "test-public-ip-address"
  }
}

resource "aws_key_pair" "test-public-key" {
  key_name   = "test-public-key"
  public_key = file("~/.ssh/test-public-key.pub")
}

resource "aws_key_pair" "test-private-key" {
  key_name   = "test-private-key"
  public_key = file("~/.ssh/test-private-key.pub")
}

data "aws_key_pair" "private-key" {
  key_name   = "private-key"
}

resource "aws_instance" "test-public-instance" {
  ami           = "ami-04e4606740c9c9381"
  instance_type = "t3.micro"
  availability_zone = "eu-north-1a"
  key_name = aws_key_pair.test-public-key.key_name

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.test-public-ni.id
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
    Name = "test-public-instance"
    test_tag = "test_tag_value"
  }
}

resource "aws_instance" "test-private-instance" {
  ami           = "ami-04e4606740c9c9381"
  instance_type = "t3.micro"
  availability_zone = "eu-north-1b"
  key_name = data.aws_key_pair.private-key.key_name

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.test-private-ni.id
  }

  tags = {
    Name = "test-private-instance"
    test_tag = "test_tag_value2"
  }
}