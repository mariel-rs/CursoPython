import os

file_directory = os.path.abspath(os.path.dirname(__file__))

def main():
    try:
        configuration = open(os.path.join(file_directory, 'config.txt'))
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")

main()