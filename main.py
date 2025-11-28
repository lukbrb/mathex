from mathex.lexer import Lexer
from mathex.parser import Parser
from mathex.interpreter import Interpreter

# def evaluate_expression(expression: str, variables: dict) -> float:
#     lexer = Lexer(expression)
#     tokens = lexer.tokenize()
#     parser = Parser(tokens)
#     ast = parser.parse()
#     evaluator = Evaluator(variables)
#     return evaluator.evaluate(ast)

# def run_example(n: int) -> None:
#     """Run the nth exemple defined in the `exemples` folder."""
#     path = f"exemples/ex{n:02d}.mathex"
#     with open(path) as f:
#         program = f.read()
#         print(f"[EXAMPLE {n:02d}]")
#         print(program, end=" = ")
#         print(evaluate_expression(program, {}))

# def run_all_examples(n_max : int) -> None:
#     for n in range(n_max):
#         run_example(n+1)

if __name__ == "__main__":
    while True:
        try:
            text = input("mathex >> ")
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            # print(list(tokens))
            parser = Parser(tokens)
            tree = parser.parse()
            if not tree: # no input
                continue
            interpreter = Interpreter()
            value = interpreter.visit(tree, {})
            print(value)
        except Exception as e:
            print(e)
