import http.server
import socketserver
import time
import os
import traceback
import keyword

PORT = 1000
OUTFILE = "index.html"

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()

    except FileNotFoundError:
        print("Error: file", filepath, "not found")

    except:
        print("Unexpected error found:")
        traceback.print_exc()

def load_settings():

    def is_identifier_valid(identifier):
        return identifier.isidentifier() and identifier not in keyword.kwlist

    def is_user_allocated(identifier):
        return identifier.isupper() and is_identifier_valid(identifier)

    try: 
        with open("serve.settings", 'r') as file:
            for index, line in enumerate(file):
                line = line.strip() 
                line = line.replace(" ", "")
                line = line.split(":", 1)
                
                identifier = line[0]
                if is_identifier_valid(identifier):
                    globals()[identifier] = line[1]
                else:
                    print("The", identifier, "identifier (line", index, "of serve.settings) is not a valid identifier")

    except FileNotFoundError:
        print("Creating serve.settings file...")
        settings = ""
        for identifier in globals():
            if(is_user_allocated(identifier)):
                settings += identifier + ": " + str(globals()[identifier]) + "\n"
        with open("serve.settings", 'w') as file:
            file.write(settings)

    except:
        print("Unexpected error found:")
        traceback.print_exc()

def init():
    load_settings()

if __name__ == "__main__":
    init()
