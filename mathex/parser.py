from typing import Iterable, Iterator, Optional
from mathex.tokens import Token, TokenType
from mathex.nodes import (FunctionNode, MinusNode, NumberNode, AddNode,
                          PlusNode, SubstractNode, MultiplyNode,
                          DivideNode, PowerNode, Node)


class Parser:
    def __init__(self, tokens: Iterable[Token]) -> None:
        self.tokens: Iterator[Token] = iter(tokens)
        self.current_token: Optional[Token]
        self.advance()

    def advance(self) -> None:
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self) -> Node:
        if self.current_token is None:
            return None
        result = self.expr()
        if self.current_token is not None:
            raise Exception("Unexpected token after expression")
        return result

    def expr(self) -> Node:
        node = self.term()
        while self.current_token is not None and self.current_token.kind in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.kind == TokenType.PLUS:
                self.advance()
                node = AddNode(left=node, right=self.term())
            elif self.current_token.kind == TokenType.MINUS:
                self.advance()
                node = SubstractNode(left=node, right=self.term())
        return node

    def term(self) -> Node:
        node = self.power()
        while self.current_token is not None and self.current_token.kind in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.kind == TokenType.MULTIPLY:
                self.advance()
                node = MultiplyNode(left=node, right=self.power())
            elif self.current_token.kind == TokenType.DIVIDE:
                self.advance()
                node = DivideNode(left=node, right=self.power())
        return node

    def factor(self) -> Node:
        token = self.current_token
        if token is None:
            raise Exception("Unexpected end of input")

        if token.kind == TokenType.LPAREN:
            self.advance()
            node = self.expr()
            if self.current_token is None or self.current_token.kind != TokenType.RPAREN:
                raise Exception("Expected ')'")
            self.advance()
            return node

        if token.kind == TokenType.FUNCTION:
            func_name = token.value
            self.advance()
            return FunctionNode(name=func_name, arg=self.factor())

        if token.kind == TokenType.NUMBER:
            self.advance()
            return NumberNode(value=token.value)

        elif token.kind == TokenType.PLUS:
            self.advance()
            return PlusNode(node=self.factor())

        elif token.kind == TokenType.MINUS:
            self.advance()
            return MinusNode(node=self.factor())

        raise Exception(f"Unexpected token: {token}")

    def power(self) -> Node:
        """
        Parse exponentiation with right-associativity.
        power := factor ( POWER power )?
        """
        node = self.factor()
        if self.current_token is not None and self.current_token.kind == TokenType.POWER:
            self.advance()
            # right-associative: parse the RHS as another power
            node = PowerNode(base=node, exponent=self.power())
        return node
