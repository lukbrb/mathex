from typing import List, Tuple

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def tokenize(self) -> List[Tuple[str, str]]:
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char in '()+-*/,':
                tokens.append((self.current_char, self.current_char))
                self.advance()
            elif self.current_char.isalpha() or self.current_char == '\\':
                tokens.append(self._read_identifier())
            elif self.current_char.isdigit() or self.current_char == '.':
                tokens.append(self._read_number())
            else:
                raise ValueError(f"Caractère inattendu: {self.current_char}")

        return tokens

    def _read_identifier(self) -> Tuple[str, str]:
        start_pos = self.pos
        if self.current_char == '\\':
            self.advance()
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char == '_'):
            self.advance()
        identifier = self.text[start_pos + 1:self.pos] if self.text[start_pos] == '\\' else self.text[start_pos:self.pos]
        return ('IDENTIFIER', identifier.lower())

    def _read_number(self) -> Tuple[str, str]:
        start_pos = self.pos
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            self.advance()
        number = self.text[start_pos:self.pos]
        return ('NUMBER', number)
