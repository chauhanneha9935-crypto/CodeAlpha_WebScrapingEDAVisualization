import pandas as pd
import os

def clean_data():
    # Get base project directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Input file path
    input_path = os.path.join(base_dir, "data", "raw", "quotes_raw.csv")

    # Output folder path
    output_folder = os.path.join(base_dir, "data", "processed")
    os.makedirs(output_folder, exist_ok=True)

    # Output file path
    output_path = os.path.join(output_folder, "quotes_cleaned.csv")

    # Read data
    df = pd.read_csv(input_path)

    # Cleaning steps
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Save cleaned file
    df.to_csv(output_path, index=False)

    print(f"\nCleaning complete! File saved at:\n{output_path}")


if __name__ == "__main__":
    clean_data()