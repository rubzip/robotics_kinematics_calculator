from typing import Literal, Optional
import sympy as sp


def get_rotation(var: str, axis: Literal['x', 'y', 'z'], dim: Literal[2, 3]) -> sy.Matrix:
    x = sy.Symbol(var)
    if dim == 2:
        return sy.rot_axis3(x)
    R3 = {
        'x': sy.rot_axis1,
        'y': sy.rot_axis2,
        'z': sy.rot_axis3,
    }[axis](x)
    H = sy.eye(4)
    H[:3, :3] = R3
    return H


def get_translation(var: str, axis: Literal['x', 'y', 'z'], dim: Literal[2, 3]) -> sy.Matrix:
    x = sy.Symbol(var)
    T = sy.eye(dim + 1)
    idx = {'x': 0, 'y': 1, 'z': 2}[axis]
    T[idx, dim] = x
    return T
