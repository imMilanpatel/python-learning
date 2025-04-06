# Test 3: Ensure value is in a list
from Automation.Excel.configs import site_credentials


def test_value_in_list():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    sample_list = [1, 2, 3, 4, 5]
    assert 3 in sample_list