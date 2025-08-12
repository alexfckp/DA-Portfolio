"""Download all project datasets.
Usage:
    python download_all.py
"""
import subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve()
projects = [
    "P1_Data_Wrangling_EDA",
    "P2_SQL_Analytics",
    "P3_Predictive_Baseline",
    "P4_Visualization_Storytelling",
]

def main():
    for p in projects:
        script = pathlib.Path(p) / "src" / "download_data.py"
        print(f"
=== {p}: downloading datasets ===")
        subprocess.check_call([sys.executable, str(script)])
    print("\nAll datasets downloaded.")

if __name__ == "__main__":
    main()