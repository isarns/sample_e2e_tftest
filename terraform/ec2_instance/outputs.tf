output "ec2_instance_id" {
  description = "The ID of the instance"
  value       = module.ec2_instance.id
}


output "ec2_instance_arn" {
  description = "The ARN of the instance"
  value       = module.ec2_instance.arn
}

output "ec2_instance_instance_state" {
  description = "The state of the instance. One of: `pending`, `running`, `shutting-down`, `terminated`, `stopping`, `stopped`"
  value       = module.ec2_instance.instance_state
}

output "aws_region" {
  description = "The aws region the ec2 was depolyed to"
  value = var.aws_region
}