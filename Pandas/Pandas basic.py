# Pandas data cleaning

import pandas as pd
df=pd.read_csv("data.csv")
print(df.to_string())       # Expecting the whole data

# Drop irrelevant columns
# df=df.drop(columns=["Legendary","No"])

# Handling missing datas # Drop not available method # Removing NaN(Not a number)
# df=df.dropna(subset=["Type2"])
#df=df.fillna({"Type2":"None"})

# Fix inconsistent values       # We can add more columns if we need
# df["Type1"]=df["Type1"].replace({"Grass":"GRASS","Fire":"FIRE"})


# Standardize text
# df["Name"]=df["Name"].str.lower()

# Fix data types
# df=["Legendary"]=df["Legendary"].astype(bool)

# Remove duplicate values
df=df.drop_duplicates()         # as of now, no duplicates in the csv file



print(df)
