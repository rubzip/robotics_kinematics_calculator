import re

PATTERN = r"([TR])\s*([xyz])\s*\((\w+)\)"

def parse(expr: str, dim: Literal[2, 3] = 3) -> Optional[sy.Matrix]:
    expressions = re.findall(PATTERN, expr)
    if not expressions:
        return None
    M = sy.eye(dim + 1)
    for operator, axis, var in expressions:
        if operator == 'R':
            M = M * get_rotation(var, axis, dim)
        elif operator == 'T':
            M = M * get_translation(var, axis, dim)
    return sy.simplify(M)
