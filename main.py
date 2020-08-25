import networkx as nx
import dfs
import logging
import datetime
import os

os.remove('ps5.log')

logging.basicConfig(
  filename='ps5.log',
  level=logging.DEBUG, 
  format='%(asctime)s %(message)s', 
  datefmt='%H:%M:%S'
  )

def main(filename):
  g = open_file(filename)
  dfs.dfs(None, None)
  return g

def open_file(filename):
  """
  Reads the text file and constructs a Graph
  filename - e.g. 'SCC.txt' or 'tiny.txt'
  """
  with open(filename) as f:
    g = nx.Graph()
    logging.debug(f'attempting to open {filename}')
    count = 0
    for line_num, line in enumerate(f.readlines()):
      edge_tuple = line.rstrip().split(' ')
      g.add_edge(*edge_tuple)
      logging.debug(line_num)
  return g

if __name__ == "__main__":
  g = main('scc.txt')