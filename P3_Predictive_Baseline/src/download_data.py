"""Download raw datasets for this project.
Usage:
    python src/download_data.py
"""
import os, sys, urllib.request, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

FILES = [{'url': 'https://raw.githubusercontent.com/ryanleeallred/datasets/master/AmesHousing.csv', 'filename': 'AmesHousing.csv', 'desc': 'Ames Housing dataset (public CSV).'}]

def fetch(url, dest):
    try:
        print(f"Downloading: {url} -> {dest}")
        urllib.request.urlretrieve(url, dest)
        print("OK")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)

def main():
    for f in FILES:
        dest = RAW / f["filename"]
        fetch(f["url"], dest)
    print("\nAll files downloaded to:", RAW)

if __name__ == "__main__":
    main()