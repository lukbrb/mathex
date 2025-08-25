from enum import StrEnum, global_enum

@global_enum
class Token(StrEnum):
    # Opérateurs arithmétiques
    PLUS  = '+'
    MINUS = '-'
    DIV   = '/'
    MUL   = '*'

    # Délimiteurs
    LPARENTHESIS = '('
    RPARENTHESIS = ')'
    LCURLY       = '{' # curly braces are used for function calls as in LateX
    RCURLY       = '}'

    # Delimiters
    ASSIGN = '='
    COMMA  = ','
    DOT    = '.'
    UNDERSCORE = '_'
    # CDOT   = "\cdot"

    # Fonctions
    # EXP = "\exp"
    # LOG = "\log"
    # COS = "\cos"
    # SIN = "\sin"
