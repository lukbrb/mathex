from mathex.lexer import Lexer
from mathex.parser import Parser
from mathex.evaluator import Evaluator

def evaluate_expression(expression: str, variables: dict) -> float:
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    evaluator = Evaluator(variables)
    return evaluator.evaluate(ast)

if __name__ == "__main__":
    expression = r"\rho + \sin(x) + \sqrt(2)"
    variables = {"rho": 1, "x": 0}
    result = evaluate_expression(expression, variables)
    print(f"Résultat: {result} for expressions {expression}")
