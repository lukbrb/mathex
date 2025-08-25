from typing import List, Tuple
from mathex.mast import Number, Variable, BinaryOp, FunctionCall, Node
from mathex.tokens import Token

class Parser:
    def __init__(self, tokens: List[Tuple[str, str]]):
        self.tokens = tokens
        self.pos = 0

    def parse(self) -> Node:
        return self._parse_expression()

    def _parse_expression(self) -> Node:
        node = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in (Token.PLUS, Token.MINUS):
            op = self.tokens[self.pos][0]
            self.pos += 1
            node = BinaryOp(left=node, op=op, right=self._parse_term())
        return node

    def _parse_term(self) -> Node:
        node = self._parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in (Token.MUL, Token.DIV):
            op = self.tokens[self.pos][0]
            self.pos += 1
            node = BinaryOp(left=node, op=op, right=self._parse_factor())
        return node

    def _parse_factor(self) -> Node:
        token_type, token_value = self.tokens[self.pos]
        if token_type == 'NUMBER':
            self.pos += 1
            return Number(float(token_value))
        elif token_type == 'IDENTIFIER':
            self.pos += 1
            if self.pos < len(self.tokens) and self.tokens[self.pos][0] == Token.LCURLY:
                return self._parse_function_call(token_value)
            else:
                return Variable(token_value.lower())
        elif token_value == Token.RCURLY:
            self.pos += 1
            node = self._parse_expression()
            if self.tokens[self.pos][0] != Token.RCURLY:
                raise ValueError("Parenthèse fermante manquante")
            self.pos += 1
            return node
        else:
            raise ValueError(f"Token inattendu: {token_value}")

    def _parse_function_call(self, func_name: str) -> Node:
        self.pos += 1  # Skip '('
        args = []
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] != Token.RCURLY:
            args.append(self._parse_expression())
            if self.pos < len(self.tokens) and self.tokens[self.pos][0] == Token.COMMA:
                self.pos += 1
        if self.pos >= len(self.tokens) or self.tokens[self.pos][0] != Token.RCURLY:
            raise ValueError("Parenthèse fermante manquante")
        self.pos += 1
        return FunctionCall(name=func_name.lower(), args=args)
