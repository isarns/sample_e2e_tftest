import pytest
import boto3


@pytest.fixture(scope="session")
def ec2_boto3_client(apply_ec2_instance_output):
    ec2_client = boto3.client("ec2", region_name=apply_ec2_instance_output["aws_region"])
    return ec2_client
