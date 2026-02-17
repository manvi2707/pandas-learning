import pandas as pd

df = pd.read_csv("Data/PokemonData.csv")

# Filtering = Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == 1] # OR u can write df[df["Legendary" == True]]
water_pokemon = df[(df["TypeA1"] == "Water") | 
                   (df["Type2"] == "Water")]

fire_flying_pokemon = df[((df["Type1"] == "Fire") & (df["Type2"] == "Flying")) | ((df["Type1"] == "Flying") & (df["Type2"] == "Fire"))]

print(fire_flying_pokemon)