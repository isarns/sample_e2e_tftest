import pytest
import tftest

PATH = "terraform"
MODULE = "vpc"
TFVARS_PATH = "terraform.tfvars"


@pytest.fixture(scope="session")
def plan_vpc():
    tf = tftest.TerraformTest(MODULE, PATH)
    tf.setup()
    plan = tf.plan(output=True, use_cache=True, tf_var_file=TFVARS_PATH)
    return plan


@pytest.fixture(scope="session")
def apply_vpc_output():
    tf = tftest.TerraformTest(MODULE, PATH)
    tf.setup()
    tf.apply(output=True, use_cache=True, tf_var_file=TFVARS_PATH)
    output = tf.output()
    yield output
    tf.destroy(auto_approve=True, use_cache=True, tf_var_file=TFVARS_PATH)
