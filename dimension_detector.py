import pandas as pd

def detect_dimensions(df: pd.DataFrame):
    dimensions = set()

    # Completeness applies to all datasets
    dimensions.add("Completeness")

    # Uniqueness: if ID-like columns exist
    id_keywords = ["id", "txn", "transaction"]
    for col in df.columns:
        if any(k in col.lower() for k in id_keywords):
            dimensions.add("Uniqueness")
            break

    # Validity: numeric or categorical columns
    for col in df.columns:
        if df[col].dtype in ["int64", "float64", "object"]:
            dimensions.add("Validity")
            break

    # Timeliness: date or timestamp columns
    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            dimensions.add("Timeliness")
            break

    # Consistency (basic): more than one column implies relationships
    if len(df.columns) > 1:
        dimensions.add("Consistency")

    return list(dimensions)
