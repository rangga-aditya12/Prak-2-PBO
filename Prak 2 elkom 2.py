# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:59:24 2024

@author: Rangga Aditya
"""

nim = input("Dua digit terakhit NIM: ")
exclude_number = int(nim[-2:])

for i in range(1, 51):
    if i != exclude_number:
        print(i, end=" ")
