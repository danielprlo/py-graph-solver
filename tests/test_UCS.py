import pytest

from py_graph_solver.UCS import UCS
from py_graph_solver.NodeParameter import NodeParameter
from py_graph_solver.AdjacencyMatrixParameter import AdjacencyMatrixParameter


def test_add_new_parameters(fixture_ucs_mock, fixture_small_adjacency_matrix):
  ucs = fixture_ucs_mock
  ucs.set_parameters(
    AdjacencyMatrixParameter('name', fixture_small_adjacency_matrix),
    NodeParameter('node', 'B'),
    NodeParameter('node', 'B'),
  )

  assert ucs.get_parameters()[0].get_value() == fixture_small_adjacency_matrix
  assert ucs.get_parameters()[1].get_value() == 'B'


def test_add_new_adjacency_matrix(fixture_ucs_mock, fixture_small_adjacency_matrix):
  ucs = fixture_ucs_mock
  parameter = AdjacencyMatrixParameter('name', fixture_small_adjacency_matrix)
  ucs.set_adjacency_matrix(parameter)
  assert ucs.get_parameters()[0].get_value() == fixture_small_adjacency_matrix


def test_add_new_node(fixture_ucs_mock):
  ucs = fixture_ucs_mock
  parameter = NodeParameter('name', '12')
  ucs.set_node(parameter)
  assert ucs.get_parameters()[1].get_value() == '12'

def test_ucs(fixture_adjacency_matrix):
  ucs = UCS(
    AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
    NodeParameter('node', '0'),
    NodeParameter('node', '7'),
  )
  result = ucs.do_algorithm()
  assert result == (20, ['0', '5', '9', '6', '7'])


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
        '0': {'3': 12, '5': 4},
        '1': {'2':13, '3': 21, '4': 1},
        '2': {'0':2},
        '3': {'5':1},
        '4': {'0':7},
        '5': {'9':3, '8':8},
        '6': {'4':2, '0':1, '7':12, '8':3},
        '7': {'0':3, '8':21, '9':2},
        '8': {},
        '9': {'6': 1, '8': 4, '5': 4},
    }


@pytest.fixture()
def fixture_small_adjacency_matrix():
  return {
    'A': ['A'],
    'B': ['B'],
  }


@pytest.fixture()
def fixture_ucs_mock():
  return UCS(
    AdjacencyMatrixParameter('name', fixture_adjacency_matrix),
    NodeParameter('node', 'A'),
    NodeParameter('node', 'B'),
  )
