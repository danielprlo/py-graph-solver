import pytest

from py_graph_solver.BFS import BFS
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
def small_adjacency_matrix_mock():
  return {
    '0': ['0'],
    '1': ['1'],
  }

@pytest.fixture()
def bfs_mock():
  return BFS(
    AdjacencyMatrixParameter('name', adjacency_matrix_mock),
    NodeParameter('node', '0')
  )

@pytest.fixture()
def adjacency_matrix_parameter():
  return AdjacencyMatrixParameter('name', adjacency_matrix_mock)

def test_add_new_parameters(bfs_mock, small_adjacency_matrix_mock):
  dfs = bfs_mock
  dfs.set_parameters(
    AdjacencyMatrixParameter('name', small_adjacency_matrix_mock),
    NodeParameter('node', '1')
  )

  assert dfs.get_parameters()[0].get_value() == small_adjacency_matrix_mock
  assert dfs.get_parameters()[1].get_value() == '1'

def test_add_new_adjacency_matrix(bfs_mock, small_adjacency_matrix_mock):
  bfs = bfs_mock
  parameter = AdjacencyMatrixParameter('name', small_adjacency_matrix_mock)
  bfs.set_adjacency_matrix(parameter)
  assert bfs.get_parameters()[0].get_value() == small_adjacency_matrix_mock


def test_add_new_node(bfs_mock, small_adjacency_matrix_mock):
  bfs = bfs_mock
  parameter = NodeParameter('name', '12')
  bfs.set_node(parameter)
  assert bfs.get_parameters()[1].get_value() == '12'

def test_bfs(adjacency_matrix_mock):
  bfs = BFS(
    AdjacencyMatrixParameter('name', adjacency_matrix_mock),
    NodeParameter('node', '0')
  )
  result = bfs.do_algorithm()

  assert result == ['0', '1', '2', '3', '4']


def test_throws_exception_if_node_does_not_exist_in_adjacency_matrix(adjacency_matrix_mock):
  with pytest.raises(Exception) as exc:
    bfs = BFS(
      AdjacencyMatrixParameter('name', adjacency_matrix_mock),
      NodeParameter('node', '-1')
    )
    bfs.do_algorithm()
  assert 'Node does not exist in the adjacency list' in str(exc)
