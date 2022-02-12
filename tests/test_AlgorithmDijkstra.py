import pytest

from py_graph_solver.Dijkstra import Dijkstra
from py_graph_solver.NodeParameter import NodeParameter
from py_graph_solver.AdjacencyMatrixParameter import AdjacencyMatrixParameter


def test_add_new_parameters(fixture_dijkstra_mock, fixture_small_adjacency_matrix):
  dijkstra = fixture_dijkstra_mock
  dijkstra.set_parameters(
    AdjacencyMatrixParameter('name', fixture_small_adjacency_matrix),
    NodeParameter('node', 'B')
  )

  assert dijkstra.get_parameters()[0].get_value() == fixture_small_adjacency_matrix
  assert dijkstra.get_parameters()[1].get_value() == 'B'


def test_add_new_adjacency_matrix(fixture_dijkstra_mock, fixture_small_adjacency_matrix):
  dijkstra = fixture_dijkstra_mock
  parameter = AdjacencyMatrixParameter('name', fixture_small_adjacency_matrix)
  dijkstra.set_adjacency_matrix(parameter)
  assert dijkstra.get_parameters()[0].get_value() == fixture_small_adjacency_matrix


def test_add_new_node(fixture_dijkstra_mock):
  dijkstra = fixture_dijkstra_mock
  parameter = NodeParameter('name', '12')
  dijkstra.set_node(parameter)
  assert dijkstra.get_parameters()[1].get_value() == '12'

def test_dfs(fixture_adjacency_matrix):
  dijkstra = Dijkstra(
    AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
    NodeParameter('node', 'V')
  )
  result = dijkstra.do_algorithm()
  print('result')
  print(result)
  assert result == {'V': {'node': 'V', 'distance': 0}, 'M': {'node': 'V', 'distance': 6}, 'CS': {'node': 'V', 'distance': 5}, 'SM': {'node': 'V', 'distance': 2}, 'F': {'node': 'SM', 'distance': 3}, 'VS': {'node': 'F', 'distance': 7}, 'SR': {'node': 'VS', 'distance': 9}, 'PV': {'node': 'F', 'distance': 7}, 'T': {'node': 'SR', 'distance': 12}}


# Fixtures
@pytest.fixture()
def fixture_unvisited_dictionary():
  COST = 0
  PREVIOUS = 1

  return {
    'A': {COST: 10, PREVIOUS: 'D'},
    'B': {COST: 9, PREVIOUS: 'C'},
    'C': {COST: 23, PREVIOUS: 'A'},
    'D': {COST: 21, PREVIOUS: 'A'}
  }


@pytest.fixture()
def fixture_adjacency_matrix():
  return {
    'V': [{'M': 6}, {'CS': 5}, {'SM': 2}],
    'M': [{'V': 6}, {'CS': 3}, {'T': 7}],
    'CS': [{'M': 3}, {'V': 5}, {'PV': 4}],
    'SM': [{'V': 2}, {'F': 1}],
    'F': [{'SM': 1}, {'PV': 4}, {'VS': 4}],
    'VS': [{'F': 4}, {'SR': 2}],
    'SR': [{'VS': 2}, {'PV': 4}, {'T': 3}],
    'PV': [{'CS': 4}, {'F': 4}, {'SR': 4}],
    'T': [{'M': 7}, {'SR': 3}],
  }


@pytest.fixture()
def fixture_small_adjacency_matrix():
  return {
    'A': ['A'],
    'B': ['B'],
  }


@pytest.fixture()
def fixture_dijkstra_mock():
  return Dijkstra(
    AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
    NodeParameter('node', 'A')
  )
