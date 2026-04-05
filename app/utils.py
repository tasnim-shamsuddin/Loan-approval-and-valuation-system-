import pandas as pd

def build_applicant_from_dict(d,expected_cols):
    df=pd.DataFrame(d, index=[0])

    for c in df.select_dtypes(include='object').columns:
        df[c].str.strip()

    #ensure if column exists 
    missing=[for c in expected_cols if c not in df.columns]

    if missing:
            raise ValueError(f"Missing columns: {missing}")
    return df[expected_cols]