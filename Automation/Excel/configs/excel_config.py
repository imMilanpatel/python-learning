import pandas as pd
import pytest


CONFIG_PATH = "Test_Runner.xlsx"
CONFIG_SHEET = "Configs"
REPORT_FILE = "report.html"

# Read Excel config
df = pd.read_excel(CONFIG_PATH, sheet_name=CONFIG_SHEET)
df = df[df['EXECUTION STATE (Y/N)'].str.upper() == 'Y']

if df.empty:
    print("No tests to run.")
    exit()

# Build test file paths
test_files = ["../test_cases/" + name.strip() + ".py" for name in df['TEST DESCRIPTION']]

# Run all selected tests at once
pytest.main(test_files + ["--html=" + REPORT_FILE, "--self-contained-html"])
