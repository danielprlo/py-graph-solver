from py_graph_solver import AdjacencyMatrixParameter, NodeParameter
from py_graph_solver.Algorithm import Algorithm


class BFS(Algorithm):
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

    visited = []
    queue = []

    result = []
    self.bfs(visited, queue, adjacency_list, node, result)
    return result

  def bfs(self, visited, queue, adjacency_list, node, result):
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
      m = queue.pop(0)
      result.append(m)

      for neighbour in adjacency_list[m]:
        if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)
