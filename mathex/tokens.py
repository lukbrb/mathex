from enum import Enum
from dataclasses import dataclass
from typing import Any


class TokenType(Enum):
    NUMBER   = 0
    PLUS     = 1
    MINUS    = 2
    MULTIPLY = 3
    DIVIDE   = 4
    LPAREN   = 5
    RPAREN   = 6


@dataclass
class Token:
    kind: TokenType
    value: Any = None

    def __repr__(self) -> str:
        return self.kind.name + (f":{self.value}" if self.value else "")
