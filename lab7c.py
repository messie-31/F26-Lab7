#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

# TO DO 1: Create numArray with 100 random numbers
num_array = np.random.randint(0, 100, 100)

# TO DO 2: Operations
print("First 10 values:", num_array[:10])
print("Last 10 values:", num_array[-10:])
print("30 values from index 21:", num_array[21:51])

# One statement: set index 50 to 65 (inclusive) to 101
num_array[50:66] = 101
print("After change:", num_array)