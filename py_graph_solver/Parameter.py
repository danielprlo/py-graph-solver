from abc import ABC, abstractmethod


# Abstract class
class Parameter(ABC):
  def __init__(self, name):
    self.name = name

  def get_name(self):
    return self.name

  @abstractmethod
  def get_value(self):
    pass

  @abstractmethod
  def set_value(self, value):
    pass


