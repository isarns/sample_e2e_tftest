import pytest
import boto3


@pytest.fixture(scope="session")
def ec2(apply_vpc_output):
    ec2 = boto3.client("ec2", region_name=apply_vpc_output["aws_region"])
    return ec2
