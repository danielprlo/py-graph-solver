from py_graph_solver.Parameter import Parameter


class AdjacencyMatrixParameter(Parameter):
  def __init__(self, name, adjacency_matrix):
    super().__init__(name)
    self.adjacency_matrix = adjacency_matrix

  def get_value(self):
    return self.adjacency_matrix

  def set_value(self, adjacency_matrix):
    self.adjacency_matrix = adjacency_matrix
