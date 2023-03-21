pytest_plugins = (
    "fixtures.vpc",
    "fixtures.ec2_instance",
    "fixtures.ec2_boto3_client",
)


def pytest_collection_modifyitems(items):
    # define the desired order of test names
    tests_order = [
        "test_vpc.py",
        "test_ec2_instance.py",
    ]
    order_map = {module_name: i for i, module_name in enumerate(tests_order)}
    items.sort(key=lambda item: order_map.get(item.fspath.basename), reverse=False)
