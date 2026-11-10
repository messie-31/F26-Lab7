#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Create Histograms.
# Usage: ./lab7h.py

# TO DO 1: Import pandas and matplotlib modules
import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(url)

# TO DO 3: Operations on the data
years = df["Year"].copy()
# Sort the years in ascending order
years = years.sort_values()

counts = years.value_counts().sort_index()
print("Number of unique years:", len(counts))
print(counts)

first10 = counts.head(10)
print("\nFirst 10 years:\n", first10)

# TO DO 2: Draw the histogram (x-axis = years, bar height = count)
plt.bar(first10.index.astype(str), first10.values, edgecolor="black", alpha=0.7)
plt.title("Number of Movies per Year (First 10 Years)")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.savefig("years.png")
plt.show()