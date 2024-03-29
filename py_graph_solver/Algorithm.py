from abc import ABC, abstractmethod


# Abstract class
class Algorithm(ABC):
  @abstractmethod
  def __init__(self):
    self.parameters = []
    pass

  def get_parameters(self):
    return self.parameters

  @abstractmethod
  def do_algorithm(self):
    pass
