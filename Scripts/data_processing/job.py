import pandas as pd
import re


file_path = r"C:\Users\manju\Downloads\employability_analytics_cleaned.csv"  
df = pd.read_csv(file_path)


def extract_core_job_title(title):

    core_titles = [
        "Data Scientist", "Data Analyst", "Machine Learning Engineer",
        "ML Engineer", "AI Engineer", "Data Engineer", "Statistician",
        "Research Scientist"
    ]
    pattern = r'\b(' + '|'.join(re.escape(t) for t in core_titles) + r')\b'
    match = re.search(pattern, title, flags=re.IGNORECASE)
    return match.group(0) if match else title.strip()


df['Job Title'] = df['Job Title'].apply(extract_core_job_title)

df.to_csv(file_path, index=False)  


print("Job titles cleaned to retain only core titles like 'Data Scientist'.")
