import pytest

from py_graph_solver import Solver, Algorithm


@pytest.fixture
def solver():
  return Solver.Solver()


@pytest.fixture()
def algorithm():
  return Algorithm

def test_set_algorithm(solver, algorithm):
  solver.set_algorithm(algorithm)

def test_get_algorithm(solver, algorithm):
  solver.set_algorithm(algorithm)
  assert solver.get_algorithm() == algorithm
