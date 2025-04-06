import pandas as pd
import pytest
import os

CONFIG_PATH = "Test_Runner.xlsx"
CONFIG_SHEET = "Configs"
REPORT_FILE = "report.html"

df_all = pd.read_excel(CONFIG_PATH, sheet_name=CONFIG_SHEET)

# Clean test names for matching and filenames
df_all['TEST DESCRIPTION CLEAN'] = df_all['TEST DESCRIPTION'].str.strip()
test_files = ["../test_cases/" + name + ".py" for name in df_all['TEST DESCRIPTION CLEAN']]

# Save enabled test names for fixture logic
enabled_tests = set(
    df_all[df_all['EXECUTION STATE (Y/N)'].str.upper() == 'Y']['TEST DESCRIPTION CLEAN'].str.lower()
)

with open("enabled_tests.tmp", "w") as f:
    f.write("\n".join(enabled_tests))

# Run all tests (disabled ones will be skipped)
pytest.main(test_files + ["--html=" + REPORT_FILE, "--self-contained-html"])

# Clean up temporary file
try:
    os.remove("enabled_tests.tmp")
except OSError as e:
    print(f"Cleanup failed: {e}")
