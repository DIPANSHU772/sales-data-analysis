
import pandas as pd

data = {
    "Name":["Amit","Ravi",None,"Neha","Rahul"],
    "Age":[23,25,None,22,24],
    "Salary":[50000,None,45000,48000,None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Data cleaning
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

print("\nCleaned Data:")
print(df)
