from py_graph_solver.Parameter import Parameter


class NodeParameter(Parameter):
  def __init__(self, name, value):
    super().__init__(name)
    self.value = value

  def get_value(self):
    return self.value

  def set_value(self, value):
    self.value = value
