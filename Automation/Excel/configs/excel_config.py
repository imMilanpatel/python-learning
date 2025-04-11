import pandas as pd
import pytest
import os

CONFIG_PATH = "Test_Runner.xlsx"
CONFIG_SHEET = "Configs"
REPORT_FILE = "report.html"
TEST_ROOT_DIR = "../test_cases/"

# Read config
df_all = pd.read_excel(CONFIG_PATH, sheet_name=CONFIG_SHEET)

# Clean test names for matching and filenames
df_all['TEST DESCRIPTION CLEAN'] = df_all['TEST DESCRIPTION'].str.strip()

# Get enabled tests
enabled_tests = set(
    df_all[df_all['EXECUTION STATE (Y/N)'].str.upper() == 'Y']['TEST DESCRIPTION CLEAN'].str.lower()
)

# Create a mapping of test name (lowercase) -> full path by scanning the entire directory tree
test_name_to_path = {}
for root, _, files in os.walk(TEST_ROOT_DIR):
    for file in files:
        if file.endswith(".py"):
            name_without_ext = os.path.splitext(file)[0].strip().lower()
            full_path = os.path.join(root, file)
            test_name_to_path[name_without_ext] = full_path

# Match test names from Excel to discovered test files
test_files_to_run = []
for test_name in df_all['TEST DESCRIPTION CLEAN']:
    name_clean = test_name.strip().lower()
    if name_clean in test_name_to_path:
        test_files_to_run.append(test_name_to_path[name_clean])
    else:
        print(f"Warning: Test script not found for '{test_name}'")

# Save enabled test names for fixture logic
with open("enabled_tests.tmp", "w") as f:
    f.write("\n".join(enabled_tests))

# Run all matched test files (disabled ones will be skipped by fixtures)
pytest.main(test_files_to_run + ["--html=" + REPORT_FILE, "--self-contained-html"])

# Clean up temporary file
try:
    os.remove("enabled_tests.tmp")
except OSError as e:
    print(f"Cleanup failed: {e}")
