import re
from sympy import sp
from .transformations import get_rotation, get_translation


PATTERN = r"([TR])\s*([xyz])\s*\((\w+)\)"

def parse(expr: str, dim: Literal[2, 3] = 3) -> Optional[sy.Matrix]:
    expressions = re.findall(PATTERN, expr)
    if not expressions:
        return None
    M = sp.eye(dim + 1)
    for operator, axis, var in expressions:
        if operator == 'R':
            M = M * get_rotation(var, axis, dim)
        elif operator == 'T':
            M = M * get_translation(var, axis, dim)
    return sp.simplify(M)
