module "ec2_instance" {
  source = "terraform-aws-modules/ec2-instance/aws"

  name = "my-ec2-instance"

  instance_type          = "t3.micro"
  subnet_id              = var.subnet_ids[0]
  vpc_security_group_ids = [var.default_security_group]

}

