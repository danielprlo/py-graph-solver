import pytest

from py_graph_solver.AdjacencyMatrixParameter import AdjacencyMatrixParameter

def test_instantiation():
  parameter = AdjacencyMatrixParameter('Matrix', { '1': '2', '3': '4'})

def test_get_adjacency_matrix_that_was_set():
  parameter = AdjacencyMatrixParameter('Matrix', { '1': '2', '3': '4'})
  assert parameter.get_value() == { '1': '2', '3': '4'}
