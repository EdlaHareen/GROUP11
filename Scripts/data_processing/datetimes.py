import pandas as pd


file_path = r"C:\Users\manju\Downloads\glassdoor_jobs_cleaned.csv"
df = pd.read_csv(file_path)


print(df['Posted Date'].unique()[:20])  



df.to_csv(r"C:\Users\manju\Downloads\glassdoor_jobs_cleaneddatetime.csv", index=False)
