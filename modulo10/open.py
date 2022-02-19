import os

file_directory = os.path.abspath(os.path.dirname(__file__))

def main():
    open(os.path.join(file_directory, "/path/to/mars.jpg"))

main()