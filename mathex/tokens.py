from enum import Enum #, StrEnum, global_enum
from dataclasses import dataclass
from typing import Any

# @global_enum
# class Token(StrEnum):
#     # Opérateurs arithmétiques
#     PLUS  = '+'
#     MINUS = '-'
#     DIV   = '/'
#     MUL   = '*'

#     # Délimiteurs
#     LPARENTHESIS = '('
#     RPARENTHESIS = ')'
#     LCURLY       = '{' # curly braces are used for function calls as in LateX
#     RCURLY       = '}'

#     # Delimiters
#     ASSIGN = '='
#     COMMA  = ','
#     DOT    = '.'
#     UNDERSCORE = '_'
#     # CDOT   = "\cdot"

#     # Fonctions
#     # EXP = "\exp"
#     # LOG = "\log"
#     # COS = "\cos"
    # SIN = "\sin"

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
