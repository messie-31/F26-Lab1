#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026/09/16
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.
quantity=6.8
stock=57.510
product=quantity*stock
print("The product of quantity and stock is: %4.0f" %product)
print("The product of quantity and stock is: %7.2f" %product)
