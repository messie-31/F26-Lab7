#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Slice 2D NumPy Arrays.
# Usage: ./lab7d.py

import numpy as np

arr_2d = np.array([[10, 20, 30, 40, 50],
                   [60, 70, 80, 90, 100],
                   [110, 120, 130, 140, 150],
                   [160, 170, 180, 190, 200]])

slice_1 = arr_2d[:2, -3:]# first two rows, last three columns
slice_2 = arr_2d[1:3, 1:3]# middle 2x2: 70, 80, 120, 130
slice_3 = arr_2d[::2, ::2]# every other row and column

print("Slice 1:\n", slice_1)
print("Slice 2:\n", slice_2)
print("Slice 3:\n", slice_3)