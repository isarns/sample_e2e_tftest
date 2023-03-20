module "vpc" {
  source             = "terraform-aws-modules/vpc/aws"
  name               = "my_vpc"
  cidr               = "10.0.0.0/16"
  azs                = ["${var.aws_region}a", "${var.aws_region}b", "${var.aws_region}c"]
  private_subnets    = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  enable_ipv6        = false
  enable_nat_gateway = false
  single_nat_gateway = true
}