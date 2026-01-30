import pandas as pd

# Load raw dataset
DATA_PATH = "../data/url_dataset.csv"
OUTPUT_PATH = "../data/clean_urls.csv"

print("📥 Loading dataset...")
df = pd.read_csv(DATA_PATH)

# Standardize column names
df.columns = df.columns.str.lower()

# Keep only required columns
df = df[["url", "type"]]

# Convert labels to binary
# legitimate -> 0, everything else -> 1
df["label"] = df["type"].apply(lambda x: 0 if "legitimate" in str(x).lower() else 1)

# Drop old type column
df = df.drop(columns=["type"])

# Remove duplicates & nulls
df = df.dropna()
df = df.drop_duplicates()

print("📊 Dataset size after cleaning:", len(df))

# Balance dataset (hackathon-friendly)
phishing = df[df["label"] == 1]
legit = df[df["label"] == 0]

sample_size = min(len(phishing), len(legit), 20000)

df_balanced = pd.concat([
    phishing.sample(sample_size, random_state=42),
    legit.sample(sample_size, random_state=42)
])

# Shuffle dataset
df_balanced = df_balanced.sample(frac=1, random_state=42)

# Save clean dataset
df_balanced.to_csv(OUTPUT_PATH, index=False)

print("✅ Clean dataset saved as clean_urls.csv")
print("🔢 Final dataset size:", len(df_balanced))
