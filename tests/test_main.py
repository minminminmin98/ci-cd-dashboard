import sys
import os

# Add the src directory to the Python module search path
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
)

from main import load_and_process_data

def test_no_duplicates():
    """
    Test if duplicate rows are removed by load_and_process_data function.

    Loads data from 'data/dataset.csv', processes it, and checks
    that there are no duplicate rows in the resulting DataFrame.
    """
    df = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
    print("Test passed: No duplicates in processed dataset.")
