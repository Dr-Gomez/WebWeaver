from multiprocessing import Array, Queue, Lock, Pipe
from os import cpu_count

def get_process_limit():
  return cpu_count() - 1


def setup_processes(outfile):
  process_lim = get_process_limit()
  print(process_lim)

  lock = Lock()
  status = Array('c', process_lim)
  intructions = Queue()
  parent_connection, child_connection = Pipe()