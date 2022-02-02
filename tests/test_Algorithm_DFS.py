import pytest

from py_graph_solver import Solver, DFS

@pytest.fixture()
def dfs():
  return DFS.DFS()

def test_dfs(dfs):
  print('aqui')
  print(dfs.do_algorithm({
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
  }, '5'))
  assert false

