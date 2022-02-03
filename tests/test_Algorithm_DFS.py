import pytest

from py_graph_solver.DFS import DFS
from py_graph_solver.NodeParameter import NodeParameter
from py_graph_solver.AdjacencyMatrixParameter import AdjacencyMatrixParameter


@pytest.fixture()
def adjacency_matrix_mock():
  return {
    '0': ['1', '2', '3', '4'],
    '1': ['0'],
    '2': ['0'],
    '3': ['0'],
    '4': ['0'],
  }

@pytest.fixture()
def adjacency_matrix_parameter():
  return AdjacencyMatrixParameter('name', adjacency_matrix_mock)


def test_dfs(adjacency_matrix_mock):
  dfs = DFS(
    AdjacencyMatrixParameter('name', adjacency_matrix_mock),
    NodeParameter('node', '0')
  )
  result = dfs.do_algorithm()

  assert result == ['0', '1', '2', '3', '4']
