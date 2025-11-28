from typing import Iterable, Optional, Iterator
from mathex.tokens import Token, TokenType

WHITESPACE = " \n\t"

class Lexer:
    def __init__(self, text: str) -> None:
        self.text: Iterator[str] = iter(text)
        self.current_char: Optional[str]
        self.advance()

    def advance(self) -> None:
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self) -> Iterable[Token]:
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char.isdigit():
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == "\\":
                # This is a LaTeX-style identifier for a function e.g. \sin, \cos, \rho.
                ident_str = ''
                self.advance()
                while self.current_char is not None and (self.current_char.isalpha()):
                    ident_str += self.current_char
                    self.advance()
                yield Token(TokenType.FUNCTION, ident_str)

            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self) -> Token:
        decimal_point_count = 0
        number_str = self.current_char if self.current_char is not None else ''
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char.isdigit()):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
            number_str += self.current_char
            self.advance()
        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str)) # TODO: int si pas de décimal ?
