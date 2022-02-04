# Context class
from py_graph_solver import Algorithm


class Solver:
  def __init__(self):
    self._algorithm = None

  def set_algorithm(self, algorithm: Algorithm):
    self._algorithm = algorithm

  def get_algorithm(self):
    return self._algorithm

  def solve(self):
    self._algorithm.do_algorithm()
