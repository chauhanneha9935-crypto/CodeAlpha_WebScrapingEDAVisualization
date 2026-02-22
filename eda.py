# TASK 2 - Exploratory Data Analysis

import pandas as pd

df = pd.read_csv("../data/processed/quotes_cleaned.csv")

print(df.head())
print(df.info())
print(df.describe())

# Example question:
# Which author appears most frequently?
print(df['author'].value_counts().head())
