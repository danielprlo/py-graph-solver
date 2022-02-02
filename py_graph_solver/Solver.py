# Context class
from py_graph_solver import Algorithm


class Solver:
  def __init__(self):
    self._algorithm = None
    self.adjacency_list = {}

  def get_adjacency_list(self):
    return self.adjacency_list

  def set_adjacency_list(self, adjacency_list):
    self.adjacency_list = adjacency_list

  def set_algorithm(self, algorithm: Algorithm):
    self._algorithm = algorithm

  def solve(self):
    self._algorithm.do_algorithm(self.adjacency_list)
