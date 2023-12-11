import os

filename = str(input("Enter File Name : "))
text = str(input("Enter Your Text : "))

with open(filename, "w") as file:
    file.write(text)
