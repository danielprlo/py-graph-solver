import pytest

from py_graph_solver.AdjacencyMatrixParameter import AdjacencyMatrixParameter

def test_instantiation():
  AdjacencyMatrixParameter('Matrix', fixture_adjacency_matrix)

def test_get_adjacency_matrix_that_was_set():
  parameter = AdjacencyMatrixParameter('Matrix', fixture_adjacency_matrix)
  assert parameter.get_value() == fixture_adjacency_matrix

# Fixtures
@pytest.fixture()
def fixture_adjacency_matrix():
  return {'1': '2', '3': '4'}
