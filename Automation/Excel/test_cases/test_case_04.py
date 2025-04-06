# Test 4: Validate dictionary key-value pair
from Automation.Excel.configs import site_credentials


def test_dict_key_value():
    print(f"Env Number: {site_credentials.environment_to_test}")
    print(f"Cert Name: {site_credentials.access_certificate_name}")
    sample_dict = {"name": "Milan", "age": 30}
    assert sample_dict["age"] == 30