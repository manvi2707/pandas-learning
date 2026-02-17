import pandas as pd

df = pd.read_csv("Data/IMDb.csv")


# Clean Columns

df["Gross"] = (
    df["Gross"]
      .replace(r"[\$,M]", "", regex=True)
)

# here we used sq brackets bcz it means even if single value i.e {'$', ',', 'M'} matched they will be removed.

df["Gross"] = pd.to_numeric(df["Gross"], errors="coerce") * 1_000_000

df["Year of Release"] = (
    df["Year of Release"]
      .str.extract(r'(\d{4})')
)

# i used regex above. r' means raw string. \d means digits and {4} means quantity. here curly bracket means we have to capture all the items present inside it. i.e a number of 4 digits.

df["Year of Release"] = pd.to_numeric(df["Year of Release"], errors="coerce")


# Highest Rated Movie]

highest_rating = df["Movie Rating"].max()
highest_rating_movie = df.loc[df["Movie Rating"] == highest_rating, "Movie Name"].iloc[0]

print("Highest Rated Movie:", highest_rating_movie)


# Highest Revenue Movie

df_revenue = df.dropna(subset=["Gross"])

highest_revenue = df_revenue["Gross"].max()
highest_revenue_movie = df_revenue.loc[df_revenue["Gross"] == highest_revenue, "Movie Name"].iloc[0]

print("Highest Revenue Movie:", highest_revenue_movie)


# Average Rating Per Year

avg_rating_per_year = (
    df.groupby("Year of Release")["Movie Rating"]
      .mean()
      .reset_index(name="Avg rating per year")
)

# by using rest_index we converted series into dataframe. we replaced year from index and made is a regular column and generated a default index (0,1,2...)
# series => [Year] -> avg rating 1D index->value
# dataframe => [Year | avg rating] 2D

print(avg_rating_per_year)


# Correlation

df_clean = df.dropna(subset=["Gross", "Movie Rating"])
correlation = df_clean["Movie Rating"].corr(df_clean["Gross"])

print(f"Correlation between Rating and Revenue: {correlation:.3f}")

