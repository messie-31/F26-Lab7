#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-09
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd

# TO DO 1: Data frames from the dictionaries
d1 = {"Apple": "Green", "Carrot": "Red", "Radish": "Purple"}
d2 = {"Okra": "Thin", "Potato": "blob", "Radish": "Round"}
d3 = {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}

df1 = pd.Series(d1).to_frame("Colour")
df2 = pd.Series(d2).to_frame("Shape")
df3 = pd.Series(d3).to_frame("Weight")
print(df1, "\n")
print(df2, "\n")
print(df3, "\n")

# Combined into one data frame (missing values show as NaN)
combined = pd.DataFrame({"Colour": d1, "Shape": d2, "Weight": d3})
print("Combined:\n", combined)

# TO DO 2: Data frame from dataframe.jpg
df_students = pd.DataFrame(
    {"student name": ["A", "B", "C", "D"],
     "student marks": [22, 344, 55, 77]},
    index=["Maths", "English", "Urdu", "Science"]
)
print(df_students)