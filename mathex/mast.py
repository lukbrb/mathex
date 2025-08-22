from dataclasses import dataclass
from typing import List, Union

@dataclass
class Number:
    value: float

@dataclass
class Variable:
    name: str

@dataclass
class BinaryOp:
    left: 'Node'
    op: str
    right: 'Node'

@dataclass
class FunctionCall:
    name: str
    args: List['Node']

Node = Union[Number, Variable, BinaryOp, FunctionCall]
