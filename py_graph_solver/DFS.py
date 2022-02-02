from py_graph_solver.Algorithm import Algorithm


class DFS(Algorithm):
  def do_algorithm(self, adjacency_list, node):
    print(adjacency_list)
    visited = set()
    result = set()
    self.dfs(visited, adjacency_list, node, result)

    return result

  def dfs(self, visited, adjacency_list, node, result):
    if node not in visited:
      print(node)
      result.add(node)
      visited.add(node)
      for neighbour in adjacency_list[node]:
        self.dfs(visited, adjacency_list, neighbour, result)
