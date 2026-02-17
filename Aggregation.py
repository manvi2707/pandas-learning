import pandas as pd

df = pd.read_csv("Data/PokemonData.csv")

# aggregation function = Reduces a set of values into a single summary value
#                        Used to summarize and analyze data
#                        Often used with grouby() function


# for Whole DataFrame
print(df.mean(numeric_only = True)) # we are finding mean of columns that contain numeric only values
print(df.sum(numeric_only = True)) # sum of all values in columns
print(df.min(numeric_only = True)) # give minimum value in the column
print(df.max(numeric_only = True)) # give maximum value in the column
print(df.count()) # count number of enteries in each column. Does NOT include NaN values.


# for Single Column
print(df["Height"].mean())
print(df["Weight"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Weight"].count())


group = df.groupby("Type1")

print(group) # group is now an object
print(group["Height"].mean()) # print avg height of each group divided by their type1 powers
print(group["Height"].sum())
print(group["Height"].count())