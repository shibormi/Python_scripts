import itertools
import os
import pandas as pd

# Metadata provided as a dictionary
metadata = {
    "S01": "Male", "S02": "Male", "S03": "Male",
    "S04": "Female", "S05": "Female", "S06": "Female"
}

# Create combinations of unique groups
groups = list(set(metadata.values()))
combinations = list(itertools.combinations(groups, 2))

# Directory to save output files
output_dir = "metadata_files"
os.makedirs(output_dir, exist_ok=True)

# Generate .tsv files for each combination
for group1, group2 in combinations:
    filename = f"{group1}vs{group2}.tsv"
    filepath = os.path.join(output_dir, filename)
    
    # Filter samples belonging to the two groups
    selected_samples = {k: v for k, v in metadata.items() if v == group1 or v == group2}
    
    # Convert to DataFrame
    df = pd.DataFrame(list(selected_samples.items()), columns=["samples", "group"])
    
    # Save to a .tsv file
    df.to_csv(filepath, sep="\t", index=False)
    print(f"Saved: {filepath}")
