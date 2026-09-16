#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026/09/16
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py

#TO-DO 1:
name="mehtaash"
str.upper(name)
age=18
print("How are you {}? Happy {}th birthday!".format(name,age)) 

#TO-DO 2:
words="The quick brown fox jumps over the lazy dog"
print("The first character is",words[0])
print("The 17th character is",words[16])

#TO-DO 3:
slice1=words[-23:-18]
print(slice1)
slice2=words[-39:-34]
print(slice2)

#TO-DO 4:
slice3=words[2:15]
print(slice3)
print(words[5:22])