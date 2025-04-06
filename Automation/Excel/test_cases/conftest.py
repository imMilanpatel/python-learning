# test_cases/conftest.py

import pytest
import pandas as pd
import os
import sys

# Add path to access site_credentials from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Configs")))
from Automation.Excel.configs import site_credentials

# Read Excel config once
CONFIG_PATH = os.path.join("..", "Configs", "Test_Runner.xlsx")
df = pd.read_excel(CONFIG_PATH, sheet_name="Configs")
df = df[df['EXECUTION STATE (Y/N)'].str.upper() == 'Y']


@pytest.fixture(autouse=True, scope="function")
def update_credentials(request):
    test_path = request.node.fspath
    file_name = os.path.basename(str(test_path))  # e.g., 'test_list_sorting.py'

    # Strip extension to match Excel
    test_key = os.path.splitext(file_name)[0].strip().lower()

    # Excel matching
    df['TEST DESCRIPTION CLEAN'] = df['TEST DESCRIPTION'].str.strip().str.lower()
    row = df[df['TEST DESCRIPTION CLEAN'] == test_key]

    if not row.empty:
        env = int(row['ENVIRONMENT'].values[0]) if not pd.isna(row['ENVIRONMENT'].values[0]) else 0
        cert = str(row['CERTIFICATE'].values[0]) if not pd.isna(row['CERTIFICATE'].values[0]) else ""
        site_credentials.set_credentials(env, cert)
        print(f"⏱️ Injected credentials for {file_name}: ENV={env}, CERT={cert}")
    else:
        print(f"⚠️ No credentials found for {file_name}")
