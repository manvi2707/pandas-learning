import pandas as pd

df = pd.read_csv("Data/PokemonData.csv")

print(df)
# To print entire datafram and not the truncated version
# Beware of doing this on large files
print(df.to_string())

# # Convert entire dataframe to JSON (records format)
# df.to_json(
#     "Data/PokemonData.json",
#     orient="records",
#     indent=4
# )

df_json = pd.read_json("Data/PokemonData.json")
print(df_json)