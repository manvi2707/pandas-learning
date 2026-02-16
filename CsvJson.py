import pandas as pd

df = pd.read_csv("Data/PokemonData.csv")

print(df)
# To print entire datafram and not the truncated version
# Beware of doing this on large files
print(df.to_string())