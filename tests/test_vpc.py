def test_plan_vpc(plan_vpc):
    pass


def test_applied_vpc_output(apply_vpc_output):
    assert apply_vpc_output["aws_region"] is not None
    assert len(apply_vpc_output["private_subnets"]) >= 1
    assert "sg-" in apply_vpc_output["default_security_group_id"]
