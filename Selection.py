import pandas as pd

df = pd.read_csv("Data/PokemonData.csv")

# Selection By Column
print(df["Name"])
# Multiple Columns
print(df[["Name", "Height", "Weight"]])

# Print entire Column
print(df["Name"].to_string())

# Print Top 5 rows Data
print(df["Name"].head())

# Print Bottom 5 rows Data
print(df["Name"].tail())


# Selection by Rows
print(df.iloc[0])

# To set a default index Column
df2 = pd.read_csv("Data/PokemonData.csv", index_col = "Name")
print(df2.loc["Pikachu"])
print(df2.loc["Charizard"])
# To set particular columns of a particular row
print(df2.loc["Bulbasaur", ["Type1", "Height", "Weight"]])
# To select range of rows to print from
print(df2.loc["Charizard":"Blastoise"])
print(df2.iloc[0:8])
print(df2.iloc[0:8:2])
print(df2.iloc[0:8:2, 0:3:2])
# print(df2.iloc[row_start_index:row_ending_index:steps, column_starting_index:column_ending_index:steps])
# ending indexs are exclusive


pokemon = input("Enter a pokemon name: ")

try:
    print(df2.loc[pokemon])
except KeyError:
    print(f"{pokemon} Not Found!")
