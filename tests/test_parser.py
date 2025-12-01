import unittest
import numpy as np
from mathex.lexer import Lexer
from mathex.parser import Parser
from mathex.interpreter import Interpreter

class TestParser(unittest.TestCase):
    def test_lexer(self) -> None:
        lexer = Lexer(r"\sin(5) + 1")
        tokens = lexer.generate_tokens()

        t_tokens = [repr(token) for token in tokens]
        expected_tokens = [
            "FUNCTION:sin",
            "LPAREN",
            "NUMBER:5.0",
            "RPAREN",
            "PLUS",
            "NUMBER:1.0"
        ]

        self.assertEqual(t_tokens, expected_tokens)

    def test_parser(self) -> None:
        lexer = Lexer(r"(1) + \sin(-1)")
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        # ctx = {"rho": 1, "x": 0}
        ctx: dict[str, float] = {}
        evaluator = Interpreter()
        result = evaluator.visit(ast, ctx)
        self.assertAlmostEqual(result, 1 + np.sin(-1))

    def test_interpreter(self) -> None:
        ctx = {"x": np.pi/2, "y": 0}
        interpreter = Interpreter()
        lexer = Lexer(r"\sin(1) + \cos(3*2)")
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        result = interpreter.visit(ast, ctx)
        self.assertAlmostEqual(result, np.sin(1) + np.cos(3*2))

    def test_interpreter_with_power(self) -> None:
        interpreter = Interpreter()
        lexer = Lexer(r"2 ^ 3 * 2")
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        result = interpreter.visit(ast, {})
        self.assertAlmostEqual(result, 2 ** 3 * 2)

    def test_interpreter_with_composed_power(self) -> None:
        interpreter = Interpreter()
        lexer = Lexer(r"2 ^ (3 * 2) - 2")
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        result = interpreter.visit(ast, {})
        self.assertAlmostEqual(result, 2 ** (3 * 2) - 2)

    def test_interpreter_with_right_associative_power(self) -> None:
        interpreter = Interpreter()
        lexer = Lexer(r"2 + 3 * (1 * 5 * (3+2)^2)")
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        result = interpreter.visit(ast, {})
        self.assertAlmostEqual(result,  2 + 3 * (1 * 5 * (3+2)**2))

if __name__ == "__main__":
    unittest.main()
