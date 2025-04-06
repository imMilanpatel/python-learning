# Test 9: Verify list sorting
from Automation.Excel.configs import site_credentials


def test_list_sorting():
    unsorted_list = [3, 1, 2]
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    assert sorted(unsorted_list) == [1, 2, 3]