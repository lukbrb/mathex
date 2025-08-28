import math
from mathex.mast import Number, Variable, BinaryOp, FunctionCall, Node

class Evaluator:
    def __init__(self, variables: dict):
        self.variables = {k.lower(): v for k, v in variables.items()}
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
        }

    def evaluate(self, node: Node) -> float:
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, Variable):
            return self.variables.get(node.name, 0)
        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
        elif isinstance(node, FunctionCall):
            args = [self.evaluate(arg) for arg in node.args]
            func = self.functions.get(node.name)
            if func is None:
                raise ValueError(f"Fonction inconnue: {node.name}")
            return func(*args)
        else:
            raise ValueError(f"Type de nœud inconnu: {type(node)}")
