import pandas as pd
import re

df = pd.read_csv(r'C:\Users\manju\Downloads\glassdoor_jobs_updated.csv')

def clean_company_name(name):
    name = re.sub(r'\s*\d+\.\d+$', '', name)
    
    name = re.sub(r'[^\w\s&.-]', '', name)  
    name = name.strip()  
    
    name = name.title()  
    
    return name

df['Company Name'] = df['Company Name'].apply(clean_company_name)

df.to_csv(r'C:\Users\manju\Downloads\glassdoor_jobs_updated.csv', index=False)

print(df[['Company Name']].head())