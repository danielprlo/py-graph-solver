from py_graph_solver import AdjacencyMatrixParameter, NodeParameter
from py_graph_solver.Algorithm import Algorithm
import queue as Q


class UCS(Algorithm):
  NODE = 'node'
  DISTANCE = 'distance'

  def __init__(self, adjacency_matrix: AdjacencyMatrixParameter, start_node: NodeParameter, end_node: NodeParameter):
    self.parameters = [adjacency_matrix, start_node, end_node]

  def set_parameters(self, adjacency_matrix: AdjacencyMatrixParameter, start_node: NodeParameter, end_node: NodeParameter):
    self.parameters = [adjacency_matrix, start_node, end_node]

  def set_adjacency_matrix(self, adjacency_matrix: AdjacencyMatrixParameter):
    self.parameters[0] = adjacency_matrix

  def set_node(self, node: NodeParameter):
    self.parameters[1] = node

  def do_algorithm(self):
    graph = self.parameters[0].get_value()
    start_node = self.parameters[1].get_value()
    end_node = self.parameters[2].get_value()

    return self.search(graph, start_node, end_node)

  def search(self, graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return

    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()

        current = node[1][len(node[1]) - 1]
        if end in node[1]:
          return node

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
