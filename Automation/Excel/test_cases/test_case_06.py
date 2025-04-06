# Test 6: Test for raising an exception
import pytest

from Automation.Excel.configs import site_credentials


def test_raises_exception():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0