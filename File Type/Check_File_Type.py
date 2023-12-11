import os

try:
    dirname = str(input("Enter Directroy Path : "))
    for filename in os.listdir(dirname):
        if os.path.isfile(os.path.join(dirname, filename)):
            extension = filename.split('.')[-1]
            print(f"Type of {filename.split('.')[0]} is {extension}")
except FileNotFoundError:
    print("Directory Not Found !")

