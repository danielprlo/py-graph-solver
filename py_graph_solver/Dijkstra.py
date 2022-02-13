from py_graph_solver import AdjacencyMatrixParameter, NodeParameter
from py_graph_solver.Algorithm import Algorithm


class Dijkstra(Algorithm):
  NODE = 'node'
  DISTANCE = 'distance'

  def __init__(self, adjacency_matrix: AdjacencyMatrixParameter, node: NodeParameter):
    self.parameters = [adjacency_matrix, node]

  def set_parameters(self, adjacency_matrix: AdjacencyMatrixParameter, node: NodeParameter):
    self.parameters = [adjacency_matrix, node]

  def set_adjacency_matrix(self, adjacency_matrix: AdjacencyMatrixParameter):
    self.parameters[0] = adjacency_matrix

  def set_node(self, node: NodeParameter):
    self.parameters[1] = node

  def do_algorithm(self):
    graph = self.parameters[0].get_value()
    node = self.parameters[1]
    return self.dijkstra(graph, node)

  def dijkstra(self, graph, node):
    distances = {}
    unvisited_nodes = []
    node_of_origin = node.get_value()

    for node in graph:
      distances[node] = {self.NODE: node_of_origin, self.DISTANCE: float('inf')}
      unvisited_nodes.append(node)
    distances[node_of_origin][self.DISTANCE] = 0

    while len(unvisited_nodes) != 0:
      current_node = self.get_next_node_with_smallest_dist(distances, unvisited_nodes)
      for neighbour_node in graph[current_node]:
        for neighbour_node_key in neighbour_node:
          if neighbour_node_key in unvisited_nodes:
            neighbour_node_distance = neighbour_node[neighbour_node_key]
            if neighbour_node_distance + distances[current_node][self.DISTANCE] < distances[neighbour_node_key][
              self.DISTANCE]:
              distances[neighbour_node_key][self.DISTANCE] = neighbour_node_distance + distances[current_node][
                self.DISTANCE]
              distances[neighbour_node_key][self.NODE] = current_node
      unvisited_nodes.remove(current_node)

    return distances

  def get_next_node_with_smallest_dist(self, distances, unvisited_nodes):
    min_distance = float('inf')
    node_min_distance = None
    for unvisited_node in unvisited_nodes:
      if distances[unvisited_node][self.DISTANCE] < min_distance:
        min_distance = distances[unvisited_node][self.DISTANCE]
        node_min_distance = unvisited_node

    return node_min_distance
