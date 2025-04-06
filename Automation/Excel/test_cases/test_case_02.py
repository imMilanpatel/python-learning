# Test 2: Verify string length
from Automation.Excel.configs import site_credentials


def test_string_length():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert len("pytest") == 6