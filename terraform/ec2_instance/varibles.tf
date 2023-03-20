variable "aws_region" {
  type        = string
  description = "The AWS region to deploy to"
}

variable "subnet_ids" {
  type        = list(string)
  description = "The vpc subnets ids"
}

variable "default_security_group" {
  type        = string
  description = "The security group to deploy the ec2 instance"
}