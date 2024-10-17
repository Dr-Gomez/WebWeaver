from multiprocessing import Array, Queue, Lock
from mmap import mmap
from .process_limits import get_process_limit

def setup_processes(outfile):
  process_lim = get_process_limit()
  print(process_lim)  

  lock = Lock()
  status = Array('c', process_lim)
  intructions = Queue()
  
  with open(outfile, 'wb') as file:
    file.write(b'\x00')
  
  with open(outfile, 'r+b') as file:
    shared = mmap(file.fileno(), 1)
    shared.close()