#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.
import pandas as pd

# TO DO 2: Create a series according to instructions given in readme.md file.
grades = pd.Series(
    ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"],
    index=["F", "D", "C", "B", "A", "A+"]
)

# TO DO 3: Perform the operations on this series given in readme.md file.
print("Series:\n", grades)

print("C and A+:\n", grades[["C", "A+"]])

print("Value only:", grades["C"])

print("Series * 2:\n", grades * 2)
# TO DO 4: Run the script.
