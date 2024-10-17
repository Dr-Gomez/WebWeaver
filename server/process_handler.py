import multiprocessing
from process_limits import get_process_limit

def setup_processes(num):
  free_process = get_process_limit()

  status = multiprocessing.Array()
  intructions = multiprocessing.Queue()
  shared = multiprocessing.Manager()