#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Work with Data Frames and CSV files.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

# Create a data frame from the raw GitHub link of the csv file
url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(url)

# Print summary of the data in the data frame
print("Summary:\n", df.describe())

# Print first 10 and last 10 rows
print("\nFirst 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

# Year of the earliest and latest movie
print("\nEarliest movie year:", df["Year"].min())
print("Latest movie year:", df["Year"].max())

# Unique values in the Genre column
print("\nUnique values in Genre:\n", df["Genre"].unique())

# Count how many movies are not made in USA
# (Origin can be like "USA | UK", so check if it contains USA)
not_usa = df[~df["Origin"].str.contains("USA")]
print("\nMovies not made in USA:", len(not_usa))

# Top 10 highest-rated movies
top10 = df.sort_values("IMDB rating", ascending=False).head(10)
print("\nTop 10 highest-rated movies:\n", top10[["Title", "IMDB rating"]])

# Step 1: function that gets the decade from the year
def get_decade(year):
    return (year // 10) * 10

# Step 2: add a decade column to the data frame
df["Decade"] = df["Year"].apply(get_decade)

# Step 3: group by decade to get the mean rating for each decade
decade_mean = df.groupby("Decade")["IMDB rating"].mean()
print("\nMean rating for each decade:\n", decade_mean)
print("\nBest decade:", decade_mean.idxmax())

# Step 4: scatter plot using matplotlib
plt.scatter(decade_mean.index, decade_mean.values)
plt.title("Mean IMDB Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Mean Rating")
plt.grid(True)
plt.savefig("decades.png")
plt.show()