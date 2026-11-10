#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-11-11
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

# TO DO 1: Copy the code from your lab7a.py file and paste here.
import numpy as np

array1 = np.arange(20, 50)
array2 = np.array(list(range(20, 50)))
print("Array1:", array1)
print("Array2:", array2)

array3 = np.arange(1, 10).reshape(3, 3)
print("Array3:\n", array3)

array4 = np.array([
    [["January", "February"], ["March", "April"], 
    ["May", "June"]], [["July", "August"], 
    ["September", "October"], ["November", "December"]]])
print("Array4:\n", array4)
print("Array4 shape:", array4.shape)

# TO DO 2: Reshape array1 to 5x6 and array2 to 2x3x5
array1 = array1.reshape(5, 6)
array2 = array2.reshape(2, 3, 5)
print("Array1 reshaped (5x6):\n", array1)
print("Array2 reshaped (2x3x5):\n", array2)

# TO DO 3: array5, a 5x5 matrix with the given diagonal and zeros elsewhere
array5 = np.diag([45, 7, 61, 8, 9])
print("Array5:\n", array5)

# TO DO 4: array6, a 7x7 matrix from a normal distribution
array6 = np.random.randn(7, 7)
print("Array6:\n", array6)
# TO DO 5: Run the script.