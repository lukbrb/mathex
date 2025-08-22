import unittest
import numpy as np
from mathex.lexer import Lexer
from mathex.parser import Parser
from mathex.evaluator import Evaluator

class TestParser(unittest.TestCase):
    def test_lexer(self):
        lexer = Lexer(r"\rho + \sin(x)")
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [('IDENTIFIER', 'rho'), ('+', '+'), ('IDENTIFIER', 'sin'), ('(', '('), ('IDENTIFIER', 'x'), (')', ')')])

    def test_parser(self):
        lexer = Lexer(r"\rho + sin(x)")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        evaluator = Evaluator({"rho": 1, "x": 0})
        result = evaluator.evaluate(ast)
        self.assertAlmostEqual(result, 1 + np.sin(0))

    def test_evaluator(self):
        evaluator = Evaluator({"x": np.pi/2, "y": 0})
        lexer = Lexer(r"sin(x) + cos(y)")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        result = evaluator.evaluate(ast)
        self.assertAlmostEqual(result, 1 + 1)

if __name__ == "__main__":
    unittest.main()
