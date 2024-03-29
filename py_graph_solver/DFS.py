from py_graph_solver import AdjacencyMatrixParameter, NodeParameter
from py_graph_solver.Algorithm import Algorithm


class DFS(Algorithm):
  def __init__(self, adjacency_matrix: AdjacencyMatrixParameter, node: NodeParameter):
    self.parameters = [adjacency_matrix, node]

  def set_parameters(self, adjacency_matrix: AdjacencyMatrixParameter, node: NodeParameter):
    self.parameters = [adjacency_matrix, node]

  def set_adjacency_matrix(self, adjacency_matrix: AdjacencyMatrixParameter):
    self.parameters[0] = adjacency_matrix

  def set_node(self, node: NodeParameter):
    self.parameters[1] = node


  def do_algorithm(self):
    adjacency_list = self.parameters[0].get_value()
    node = self.parameters[1].get_value()

    if node not in adjacency_list:
      raise Exception('Node does not exist in the adjacency list')

    visited = set()
    result = []
    self.dfs(visited, adjacency_list, node, result)
    return result

  def dfs(self, visited, adjacency_list, node, result):
    if node not in visited:
      visited.add(node)
      result.append(node)
      for neighbour in adjacency_list[node]:
        self.dfs(visited, adjacency_list, neighbour, result)
