import pytest

from Automation.Excel.configs import site_credentials


# Test 1: Check addition function
def test_addition():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert 2 + 2 == 4


