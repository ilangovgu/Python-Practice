import pandas as pd

df = pd.read_csv("data.csv")

# Filtering = Keeping the rows that match a condition

# Filter by Height
tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

# Filter by Weight
heavy_pokemon = df[df["Weight"] > 100]
# print(heavy_pokemon)

# Filter by Legendary status
legendary_pokemon = df[df["Legendary"] == 1]
# print(legendary_pokemon)

# Filter by Type (Water as primary or secondary type)
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)