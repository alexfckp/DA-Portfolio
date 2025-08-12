# Utility helpers for notebooks

import os
import pandas as pd
from typing import Tuple

def ensure_dirs(*paths: str) -> None:
    for p in paths:
        os.makedirs(p, exist_ok=True)

def load_csv(path: str, **kwargs) -> pd.DataFrame:
    df = pd.read_csv(path, **kwargs)
    return df

def save_df(df: pd.DataFrame, path: str, index=False) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=index)

def memory_report(df: pd.DataFrame) -> pd.Series:
    s = (df.memory_usage(deep=True) / 1024**2).round(3)
    s.loc["TOTAL_MB"] = s.sum()
    return s
