import pytest

from py_graph_solver.NodeParameter import NodeParameter

def test_instantiation():
  parameter = NodeParameter('Node', 'a')

def test_get_node_that_was_set():
  parameter = NodeParameter('Matrix', 'a')
  assert parameter.get_value() == 'a'
