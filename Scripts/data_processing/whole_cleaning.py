import pandas as pd
import numpy as np
import re


df = pd.read_csv(r'C:\Users\manju\Downloads\glassdoor_jobs_updated.csv')


print(df.head())


df.replace(-1, np.nan, inplace=True)
df.replace("", np.nan, inplace=True)

# Drop rows where critical columns (e.g., Job Title, Company Name) are missing
df.dropna(subset=["Job Title", "Company Name"], inplace=True)




# Function to clean job descriptions
def clean_text(text):
    if pd.isna(text):
        return ""
    # Remove special characters and extra whitespace
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase
    return text

# Apply the function to the Job Description column
df["Job Description"] = df["Job Description"].apply(clean_text)




# Standardize Industry and Sector columns
df["Industry"] = df["Industry"].str.strip().str.title()
df["Sector"] = df["Sector"].str.strip().str.title()

# Standardize Type of Ownership
df["Type of ownership"] = df["Type of ownership"].str.strip().str.title()


# Drop duplicate rows based on Job Title, Company Name, and Location Type
df.drop_duplicates(subset=["Job Title", "Company Name", "Location Type"], inplace=True)


# Ensure Posted Date is in a consistent format (YYYY-MM-DD)
df["Posted Date"] = pd.to_datetime(df["Posted Date"], errors="coerce")

# Convert Rating to float
df["Rating"] = df["Rating"].astype(float)


# Save the cleaned dataset to a new CSV file
df.to_csv(r'C:\Users\manju\Downloads\glassdoor_jobs_cleaned1.csv', index=False)

# Displays the cleaned dataset
print(df.head())
print("Data cleaning complete! Cleaned data saved to 'glassdoor_jobs_cleaned.csv'.")