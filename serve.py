from server import *

PORT = 1000
ENTRY = "entry.js"
OUTFILE = "index.html"

def init():
    load_settings(globals())

if __name__ == "__main__":
    init()
