# Test 5: Assert type of variable
from Automation.Excel.configs import site_credentials


def test_variable_type():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert isinstance(123, int)