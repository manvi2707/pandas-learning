import pandas as pd

df = pd.read_csv("Data/PokemonData.csv")

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect or irrelevant data.
#                 ~75% of work done with Pandas is Data Cleaning.


# 1. drop irrelevant columns
df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data (remove the rows that have NaN values in given columns)
df = df.dropna(subset=["Type2"]) # remove the rows that have NaN values in given columns
df = df.fillna({"Type2": "None"}) # replaced NaN missing values with another value

# 3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE",
                                   "Water": "WATER"}) # replace given value in a column to another value. Grass -> GRASS

# 4. Standardize text
df["Name"] = df["Name"].str.lower()

# 5. Fix Data Types
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())