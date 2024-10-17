from server import *

PORT = 1000
ENTRY = "entry.js"
OUTFILE = "webweaver.html"

def init():
    load_settings(globals())
    setup_processes(OUTFILE)

if __name__ == "__main__":
    init()
