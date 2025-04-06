# Test 7: Check substring in a string
from Automation.Excel.configs import site_credentials


def test_substring():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert "py" in "pytest"