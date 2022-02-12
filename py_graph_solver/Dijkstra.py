from py_graph_solver import AdjacencyMatrixParameter, NodeParameter
from py_graph_solver.Algorithm import Algorithm
import copy


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
    # grafo ponderado
    graph = self.parameters[0].get_value()
    node = self.parameters[1]
    return self.dijkstra(graph, node)

  def dijkstra(self, graph, node):
    distances = {}
    unvisitedNodes = []
    nodeOfOrigin = node.get_value()

    for vertex in graph:
      distances[vertex] = {self.NODE: nodeOfOrigin, self.DISTANCE: float('inf')}
      unvisitedNodes.append(vertex)
    distances[nodeOfOrigin][self.DISTANCE] = 0
    while len(unvisitedNodes) != 0:
      currentNode = self.get_next_node_with_smallest_dist(distances, unvisitedNodes)
      #TODO get the fucking key well
      for neighbour_node in graph[currentNode]:
        for neighbour_node_key in neighbour_node:
          if neighbour_node_key in unvisitedNodes:
            neighbour_node_distance = neighbour_node[neighbour_node_key]
            if neighbour_node_distance + distances[currentNode][self.DISTANCE] < distances[neighbour_node_key][self.DISTANCE]:
              distances[neighbour_node_key][self.DISTANCE] = neighbour_node_distance + distances[currentNode][self.DISTANCE]
              distances[neighbour_node_key][self.NODE] = currentNode
      unvisitedNodes.remove(currentNode)

    return distances

  def get_next_node_with_smallest_dist(self, distances, unvisitedNodes):
    minDistance = float('inf')
    nodeMinDistance = None
    for unvisitedNode in unvisitedNodes:
      if distances[unvisitedNode][self.DISTANCE] < minDistance:
        minDistance = distances[unvisitedNode][self.DISTANCE]
        nodeMinDistance = unvisitedNode

    return nodeMinDistance
