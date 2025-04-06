# Test 8: Test range boundaries
from Automation.Excel.configs import site_credentials


def test_range_boundary():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert 5 in range(1, 10)