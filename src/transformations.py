from typing import Literal
import sympy as sp


def get_rotation(var: str, axis: Literal['x', 'y', 'z'], dim: Literal[2, 3]) -> sp.Matrix:
    x = sp.Symbol(var)
    if dim == 2:
        return sp.rot_axis3(x)
    rot = {
        'x': sp.rot_axis1,
        'y': sp.rot_axis2,
        'z': sp.rot_axis3,
    }[axis](x)
    rot_homogenous = sp.eye(4)
    rot_homogenous[:3, :3] = rot
    return rot_homogenous


def get_translation(var: str, axis: Literal['x', 'y', 'z'], dim: Literal[2, 3]) -> sp.Matrix:
    x = sp.Symbol(var)
    translation = sp.eye(dim + 1)
    idx = {'x': 0, 'y': 1, 'z': 2}[axis]
    translation[idx, dim] = x
    return translation


def get_euler_matrix(yaw: str = "psi", pitch: str = "theta", roll: str = "phi", axes: str = "zyx"):
    if len(axes) != 3:
        raise ValueError("axes debe tener 3 caracteres, ej: 'zyx'")

    yaw = sp.Symbol(yaw)
    pitch = sp.Symbol(pitch)
    roll = sp.Symbol(roll)

    R = {
        'x': sp.rot_axis1,
        'y': sp.rot_axis2,
        'z': sp.rot_axis3,
    }

    r1 = R[axes[0]](yaw)
    r2 = R[axes[1]](pitch)
    r3 = R[axes[2]](roll)

    return r1 * r2 * r3
