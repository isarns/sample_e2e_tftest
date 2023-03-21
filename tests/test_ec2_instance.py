def test_plan_ec2_instance(plan_ec2_instance):
    pass


def test_applied_ec2_instance_output(apply_ec2_instance_output):
    assert apply_ec2_instance_output["aws_region"] is not None
    assert apply_ec2_instance_output["ec2_instance_id"] is not None


def test_instance_running(ec2_boto3_client, apply_ec2_instance_output):
    response = ec2_boto3_client.describe_instances(
        InstanceIds=[apply_ec2_instance_output["ec2_instance_id"]]
    )
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
    assert state == "running"
