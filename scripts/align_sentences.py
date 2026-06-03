import csv

# -------------------------
# FILE PATHS
# -------------------------
rakhine_file = "raw_data/rakhine_text.txt"
english_file = "raw_data/english_text.txt"
output_file = "data/train.csv"

# -------------------------
# READ FILES
# -------------------------
with open(rakhine_file, "r", encoding="utf-8") as f:
    rakhine_lines = [line.strip() for line in f if line.strip()]

with open(english_file, "r", encoding="utf-8") as f:
    english_lines = [line.strip() for line in f if line.strip()]

# -------------------------
# ALIGN SENTENCES
# -------------------------
pairs = []

min_len = min(len(rakhine_lines), len(english_lines))

if len(rakhine_lines) != len(english_lines):
    print(f"⚠️ Warning: mismatch detected!")
    print(f"Rakhine lines: {len(rakhine_lines)}")
    print(f"English lines: {len(english_lines)}")
    print(f"Using only {min_len} aligned pairs")

for i in range(min_len):
    r = rakhine_lines[i]
    e = english_lines[i]

    # basic safety check
    if r and e:
        pairs.append([r, e])

# -------------------------
# WRITE CSV OUTPUT
# -------------------------
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    # IMPORTANT: lowercase for Hugging Face consistency
    writer.writerow(["rakhine", "english"])

    writer.writerows(pairs)

print(f"Done! Created {output_file} with {len(pairs)} sentence pairs.")
