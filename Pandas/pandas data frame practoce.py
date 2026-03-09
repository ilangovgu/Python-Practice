import pandas as pd

# Create initial DataFrame
data = {"Name": ["siva", "murali", "thanapal"],
    "Age": [30, 32, 32]}
df = pd.DataFrame(data, index=["Emp 1", "Emp 2", "Emp 3"])

# Add a new column
df["Job"] = ["engineer", "driver", "accountant"]

# Add new rows
new_rows = pd.DataFrame([{"Name": "sunil", "Age": 32, "Job": "banking"},
             {"Name": "bas", "Age": 31, "Job": "teacher"}],
            index=["Emp 4", "Emp 5"])

df = pd.concat([df, new_rows])
print(df)