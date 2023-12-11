import os

try:
    filename = str(input("Enter File Name : "))
    print_line = int(input("Enter Line Numbers : "))
    line_count = 1
    with open (filename, "r") as file:
        for line in file:
            if line_count == print_line:
                print(line, end="")
                break
            line_count += 1
except FileNotFoundError:
    print("File Not Found !")
