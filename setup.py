from setuptools import find_packages, setup

setup(
  name='py_graph_solver',
  packages=find_packages(include=['py_graph_solver']),
  version='0.1.0',
  description='Python graph solver for students',
  author='Daniel Perez - @shake93',
  license='MIT',
  install_requires=[],
  setup_requires=['pytest-runner'],
  tests_require=['pytest==4.4.1'],
  test_suite='tests'
)
