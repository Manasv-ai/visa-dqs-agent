import pandas as pd
import numpy as np
from datetime import datetime

def completeness_score(df):
    return round(100 * (1 - df.isnull().sum().sum() / df.size), 2)

def uniqueness_score(df):
    duplicates = df.duplicated().sum()
    return round(100 * (1 - duplicates / len(df)), 2)

def validity_score(df):
    valid_cells = 0
    total_cells = 0

    for col in df.columns:
        series = df[col]
        total_cells += len(series)

        if series.dtype in ['int64', 'float64']:
            valid_cells += series.notnull().sum()
        else:
            valid_cells += series.astype(str).str.len().gt(0).sum()

    return round(100 * valid_cells / total_cells, 2)

def timeliness_score(df):
    date_cols = df.select_dtypes(include=['datetime64', 'object']).columns
    for col in date_cols:
        try:
            dates = pd.to_datetime(df[col])
            freshness = (datetime.now() - dates.max()).days
            return max(0, 100 - freshness)
        except:
            continue
    return None

def compute_dqs(df):
    scores = {
        "Completeness": completeness_score(df),
        "Uniqueness": uniqueness_score(df),
        "Validity": validity_score(df)
    }

    time_score = timeliness_score(df)
    if time_score is not None:
        scores["Timeliness"] = time_score

    composite = round(sum(scores.values()) / len(scores), 2)
    return scores, composite
