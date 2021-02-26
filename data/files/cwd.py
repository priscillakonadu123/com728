# information about current working directory
import os
def cwd():
    path = os.getcwd()

    print()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")

    for file in os.listdir(path):
        print(file)

def run():
    print("Processing...")

run()
