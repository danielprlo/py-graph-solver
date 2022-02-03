import pytest

from py_graph_solver import DFS

@pytest.fixture()
def dfs():
  return DFS.DFS()

def test_dfs(dfs):
  result = dfs.do_algorithm({
    '0' : ['1','2','3','4'],
    '1' : ['0'],
    '2' : ['0'],
    '3' : ['0'],
    '4' : ['0'],
  }, '0')

  assert result == ['0', '1', '2', '3', '4']


