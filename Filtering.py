import pandas as pd

# Load the dataset
file_path = r"C:\Users\manju\Downloads\glassdoor_jobs_updated.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

# Filter dataset for Texas locations
df_texas = df[df["Location"].str.contains(", TX", na=False, case=False)]

# Save the filtered dataset
output_file = r"C:\Users\manju\Downloads\Texas_jobs_filtered.csv"
df_texas.to_csv(output_file, index=False)

print("Filtered Texas jobs saved as 'Texas_jobs_filtered'.")
