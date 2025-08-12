# fetch_data.py
"""
Script to download the dataset for COVID-19 Data Repository by CSSE at Johns Hopkins University.
Run this script from the project root with:
    python src/fetch_data.py
"""

import os
import pathlib
import requests

RAW = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

print("=== Fetching dataset for: COVID-19 Data Repository by CSSE at Johns Hopkins University ===")
print("Source: https://github.com/CSSEGISandData/COVID-19")

# NOTE: This dataset may require manual download if hosted on Kaggle or GitHub.
# For Kaggle datasets, install kaggle API: pip install kaggle
# and authenticate: kaggle datasets download -d <dataset-path> -p data/raw --unzip

# Example generic download (replace with real file URL if direct link available)
# url = "https://example.com/data.csv"
# response = requests.get(url)
# if response.status_code == 200:
#     with open(RAW / "dataset.csv", "wb") as f:
#         f.write(response.content)
#     print("Download complete.")
# else:
#     print(f"Failed to fetch dataset: {response.status_code}")

print(">> If this dataset is from Kaggle, please use Kaggle CLI to download it.")
