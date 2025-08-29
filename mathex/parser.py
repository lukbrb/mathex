from typing import List
from mathex.tokens import Token, TokenType
from mathex.nodes import (MinusNode, NumberNode, AddNode, 
                          PlusNode, SubstractNode, MultiplyNode, 
                          DivideNode, Node)


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = iter(tokens)
        self.current_token = None
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
        node = self.factor()
        while self.current_token is not None and self.current_token.kind in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.kind == TokenType.MULTIPLY:
                self.advance()
                node = MultiplyNode(left=node, right=self.factor())
            elif self.current_token.kind == TokenType.DIVIDE:
                self.advance()
                node = DivideNode(left=node, right=self.factor()) 
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
    