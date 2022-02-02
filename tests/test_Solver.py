import pytest

from py_graph_solver import Solver, Algorithm


@pytest.fixture
def solver():
  return Solver.Solver()


@pytest.fixture()
def algorithm():
  return Algorithm

def test_adjacency_list_is_empty(solver):
  assert len(solver.get_adjacency_list()) == 0


def test_send_adjacency_list_to_solver(solver):
  solver.set_adjacency_list({
    1: [1],
    2: [2],
    3: [3]
  })

def test_get_same_adjacency_list_is_set(solver):
  solver.set_adjacency_list({
    1: [1],
    2: [2],
    3: [3]
  })
  assert solver.get_adjacency_list() == {
    1: [1],
    2: [2],
    3: [3]
  }

def test_set_algorithm(solver, algorithm):
  solver.set_algorithm(algorithm)
