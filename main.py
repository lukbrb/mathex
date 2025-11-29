from mathex.lexer import Lexer
from mathex.parser import Parser
from mathex.interpreter import Interpreter


if __name__ == "__main__":
    while True:
        try:
            text = input("mathex >> ")
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
            if not tree: # no input
                continue
            interpreter = Interpreter()
            value = interpreter.visit(tree, {})
            print(value)
        except Exception as e:
            print(e)
