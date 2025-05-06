import pandas as pd
import random

file_path = r"C:\Users\manju\Downloads\employability_analytics_cleaned.csv"
df = pd.read_csv(file_path)

skills_list = [
    "Python", "TensorFlow", "AWS", "Matplotlib", "SQL", "Data Analysis",
    "Machine Learning", "Power BI", "Tableau", "Docker", "Azure", "JavaScript",
    "Cloud Computing", "Deep Learning", "Natural Language Processing", "R", "Hadoop",
     "Excel","Data Visualization", "Statistics", "Big Data", "PyTorch", "Natural Language Processing", "Model Deployment", "Spark",
     "Data Cleaning","Git", "Azure", "Data Warehousing","ETL","Snowflake"

]


def assign_multiple_skills():
    return ", ".join(random.sample(skills_list, random.randint(3, 4)))

df['Extracted Skills'] = df.apply(lambda row: assign_multiple_skills(), axis=1)

output_file_path = r"C:\Users\manju\Downloads\employability_analytics_cleaned.csv"
df.to_csv(output_file_path, index=False)

print("Extracted Skills")
