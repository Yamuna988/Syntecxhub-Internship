import pandas as pd
import argparse
from pathlib import Path
import logging
import sys

# ----------------- Logging -----------------
logging.basicConfig(
    filename="converter_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------- Functions -----------------
def create_sample_csv(csv_path):
    sample_data = {
        "Name": ["Yamuna", "Ravi"],
        "Email": ["yamuna@example.com", "ravi@example.com"],
        "Date Joined": ["2026-03-01", "2026-03-03"],
        "Score": [85, 90]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv(csv_path, index=False)
    print(f"ℹ️ Sample CSV created at '{csv_path}'")
    logging.info(f"Sample CSV created at '{csv_path}'")

def clean_and_convert(input_file, output_file):
    csv_path = Path(input_file)

    # If CSV does not exist, create a sample CSV
    if not csv_path.exists():
        print(f"⚠️ Input file '{input_file}' not found. Creating a sample CSV.")
        create_sample_csv(csv_path)

    try:
        # Read CSV with automatic date parsing
        df = pd.read_csv(csv_path, parse_dates=True)

        # Basic cleaning
        df = df.drop_duplicates()  # remove duplicate rows
        df = df.fillna('')         # replace NaN with empty string

        # Normalize column names
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

        # Export to Excel
        output_path = Path(output_file)
        df.to_excel(output_path, index=False, engine='openpyxl')

        print(f"✅ Successfully converted '{input_file}' → '{output_file}'")
        logging.info(f"Converted {input_file} → {output_file}")

    except Exception as e:
        print(f"❌ Failed to convert '{input_file}': {e}")
        logging.error(f"Failed to convert {input_file}: {e}")
        sys.exit(1)

# ----------------- CLI -----------------
def main():
    parser = argparse.ArgumentParser(description="CSV → Excel Converter (auto sample CSV)")
    parser.add_argument('-i', '--input', default="sample.csv", help="Input CSV file path")
    parser.add_argument('-o', '--output', default="output.xlsx", help="Output Excel file path")

    args = parser.parse_args()
    clean_and_convert(args.input, args.output)

if __name__ == "__main__":
    main()