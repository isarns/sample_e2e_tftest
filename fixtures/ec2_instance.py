import pytest
import tftest

PATH = "terraform"
MODULE = "ec2_instance"


@pytest.fixture(scope="session")
def vars_from_vpc(apply_vpc_output):
    return {
        "aws_region": apply_vpc_output["aws_region"],
        "subnet_ids": apply_vpc_output["private_subnets"],
        "default_security_group": apply_vpc_output["default_security_group_id"],
    }


@pytest.fixture(scope="session")
def plan_ec2_instance(vars_from_vpc):
    tf = tftest.TerraformTest(MODULE, PATH)
    tf.setup()
    plan = tf.plan(output=True, use_cache=True, tf_vars=vars_from_vpc)
    return plan


@pytest.fixture(scope="session")
def apply_ec2_instance_output(vars_from_vpc):
    tf = tftest.TerraformTest(MODULE, PATH)
    tf.setup()
    tf.apply(output=True, use_cache=True, tf_vars=vars_from_vpc)
    output = tf.output()
    yield output
    tf.destroy(auto_approve=True, use_cache=True, tf_vars=vars_from_vpc)
