import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Drop missing values early
df = df.dropna(subset=["rakhine", "english"])

# Strip whitespace
df["rakhine"] = df["rakhine"].astype(str).str.strip()
df["english"] = df["english"].astype(str).str.strip()

# Remove empty strings + accidental "nan"
df = df[
    (df["rakhine"] != "") &
    (df["english"] != "") &
    (df["rakhine"].str.lower() != "nan") &
    (df["english"].str.lower() != "nan")
]

# Remove very short sentences
df = df[df["rakhine"].str.len() > 1]
df = df[df["english"].str.len() > 1]

# Remove duplicates
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("data/train_clean.csv", index=False)

print("Cleaning completed. Saved to data/train_clean.csv")
