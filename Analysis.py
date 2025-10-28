import pandas as pd

# Read CSV file
data = pd.read_csv("data.csv")

# Display first 5 rows
print(data.head())

# Find average of a column (example: 'Salary')
if 'Salary' in data.columns:
    print("Average Salary:", data['Salary'].mean())
