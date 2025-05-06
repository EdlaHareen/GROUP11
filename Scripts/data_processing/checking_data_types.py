import pandas as pd

file_path = r'C:\Users\manju\Downloads\glassdoor_jobs_cleaneddatetime.csv'
df = pd.read_csv(file_path)

print(df.dtypes)