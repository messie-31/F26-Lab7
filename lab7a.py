#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Create Arrays.
# Usage: ./lab7a.py

import numpy as np

# TO DO 1: Create array1 and array2 (integers 20 to 49) in two ways
array1 = np.arange(20, 50)
array2 = np.array(list(range(20, 50)))
print("Array1:", array1)
print("Array2:", array2)

# TO DO 2: Create array3, a 3x3 matrix with values 1 to 9
array3 = np.arange(1, 10).reshape(3, 3)
print("Array3:\n", array3)

# TO DO 3: Create array4, a 2x3x2 matrix of month names
array4 = np.array([
    [["January", "February"], ["March", "April"], ["May", "June"]],
    [["July", "August"], ["September", "October"], ["November", "December"]]])
print("Array4:\n", array4)
print("Array4 shape:", array4.shape)