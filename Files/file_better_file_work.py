# w writing a appending r reading r+ reading/writing
import os.path
filename = "./datax.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")