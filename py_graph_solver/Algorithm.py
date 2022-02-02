from abc import ABC, abstractmethod


# Interface
class Algorithm(ABC):
  @abstractmethod
  def do_algorithm(self, matrix, node):
    pass
