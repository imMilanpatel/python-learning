# Test 10: Validate custom function
from Automation.Excel.configs import site_credentials


def test_custom_function():
    def multiply(a, b):
        return a * b

    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert multiply(3, 4) == 12