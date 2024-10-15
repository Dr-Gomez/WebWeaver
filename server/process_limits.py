import os

def get_process_limit():
  return os.cpu_count() -1
