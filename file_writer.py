import os


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
