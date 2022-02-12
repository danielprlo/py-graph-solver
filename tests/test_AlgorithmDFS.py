import pytest

from py_graph_solver.DFS import DFS
from py_graph_solver.NodeParameter import NodeParameter
from py_graph_solver.AdjacencyMatrixParameter import AdjacencyMatrixParameter


def test_add_new_parameters(fixture_dfs_mock, fixture_small_adjacency_matrix):
  dfs = fixture_dfs_mock
  dfs.set_parameters(
    AdjacencyMatrixParameter('name', fixture_small_adjacency_matrix),
    NodeParameter('node', '1')
  )

  assert dfs.get_parameters()[0].get_value() == fixture_small_adjacency_matrix
  assert dfs.get_parameters()[1].get_value() == '1'


def test_add_new_adjacency_matrix(fixture_dfs_mock, fixture_small_adjacency_matrix):
  dfs = fixture_dfs_mock
  parameter = AdjacencyMatrixParameter('name', fixture_small_adjacency_matrix)
  dfs.set_adjacency_matrix(parameter)
  assert dfs.get_parameters()[0].get_value() == fixture_small_adjacency_matrix


def test_add_new_node(fixture_dfs_mock):
  dfs = fixture_dfs_mock
  parameter = NodeParameter('name', '12')
  dfs.set_node(parameter)
  assert dfs.get_parameters()[1].get_value() == '12'


def test_dfs(fixture_adjacency_matrix):
  dfs = DFS(
    AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
    NodeParameter('node', '0')
  )
  result = dfs.do_algorithm()

  assert result == ['0', '1', '2', '3', '4']


def test_throws_exception_if_node_does_not_exist_in_adjacency_matrix(fixture_adjacency_matrix):
  with pytest.raises(Exception) as exc:
    dfs = DFS(
      AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
      NodeParameter('node', '-1')
    )
    dfs.do_algorithm()
  assert 'Node does not exist in the adjacency list' in str(exc)


# Fixtures
@pytest.fixture()
def fixture_adjacency_matrix():
  return {
    '0': ['1', '2', '3', '4'],
    '1': ['0'],
    '2': ['0'],
    '3': ['0'],
    '4': ['0'],
  }


@pytest.fixture()
def fixture_small_adjacency_matrix():
  return {
    '0': ['0'],
    '1': ['1'],
  }


@pytest.fixture()
def fixture_dfs_mock():
  return DFS(
    AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
    NodeParameter('node', '0')
  )


@pytest.fixture()
def fixture_adjacency_matrix_parameter():
  return AdjacencyMatrixParameter('name', fixture_adjacency_matrix)
