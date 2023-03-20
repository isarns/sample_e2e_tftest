pytest_plugins = (
    "fixtures.vpc",
    "fixtures.ec2_instance",
    "fixtures.ec2",
)


def pytest_collection_modifyitems(items):
    # define the desired order of test module names
    module_order = [
        "test_vpc.py",
        "test_ec2_instance.py",
    ]
    # create a dictionary that maps module names to their index in module_order
    order_map = {module_name: i for i, module_name in enumerate(module_order)}
    # sort the test items based on their module names using the order_map dictionary
    items.sort(key=lambda item: order_map.get(item.fspath.basename), reverse=False)
