import traceback
from multiprocessing import process

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()

    except FileNotFoundError:
        print("Error: file", filepath, "not found")

    except:
        print("Unexpected error found:")
        traceback.print_exc()

def process_file(filepath, content):
    content = read_file(filepath)

