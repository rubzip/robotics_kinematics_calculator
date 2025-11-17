import sympy as sp

def get_position(transformation: sp.Matrix, center: sp.Matrix = None) -> sp.Matrix:
  if center is None:
    center = sp.Zeros(len(transformation), 1)
  return transformation * center

def get_jacobian(transformation: sp.Matrix, symbols: sp.Matrix):
  return transformation.jacobian(symbols)
