import pandas as pd
import os

def load_and_process_data(
    filepath: str = "data/dataset.csv",
    output_path: str = "data/processed_dataset.csv"
) -> pd.DataFrame:
    """
    Loads the dataset, removes duplicate rows, and saves the processed dataset.

    Args:
        filepath (str): Path to the input dataset.
        output_path (str): Path to save the processed dataset.

    Returns:
        pd.DataFrame: Processed DataFrame with no duplicates.
    """
    # Check if the input file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found: {filepath}")

    # Load the dataset
    df = pd.read_csv(filepath)
    print(f"Original dataset shape: {df.shape}")

    # Remove duplicate rows
    df = df.drop_duplicates()
    print(f"Dataset shape after removing duplicates: {df.shape}")

    # Save the processed dataset
    output_path = os.path.abspath(output_path)
    try:
        print(f"Attempting to save to: {output_path}")
        df.to_csv(output_path, index=False)
        print("Processed dataset saved successfully!")
    except Exception as e:
        print(f"Failed to save file. Error: {e}")

    return df

if __name__ == "__main__":
    load_and_process_data()
