from dataclasses import dataclass
from typing import Any, Union


@dataclass
class NumberNode:
    value: float
    def __repr__(self) -> str:
        return f"{self.value}"


@dataclass
class AddNode:
    left: Any
    right: Any
    def __repr__(self) -> str:
        return f"({self.left} + {self.right})"


@dataclass
class SubstractNode:
    left: Any
    right: Any
    def __repr__(self) -> str:
        return f"({self.left} - {self.right})"


@dataclass
class MultiplyNode:
    left: Any
    right: Any
    def __repr__(self) -> str:
        return f"({self.left} * {self.right})"


@dataclass
class DivideNode:
    left: Any
    right: Any
    def __repr__(self) -> str:
        return f"({self.left} / {self.right})"


@dataclass
class PowerNode:
    base: Any
    exponent: Any
    def __repr__(self) -> str:
        return f"({self.base} ^ {self.exponent})"


@dataclass
class PlusNode: # Unary plus
    node: Any
    def __repr__(self) -> str:
        return f"(+{self.node})"


@dataclass
class MinusNode: # Unary minus
    node: Any
    def __repr__(self) -> str:
        return f"(-{self.node})"


@dataclass
class FunctionNode:
    arg: Any
    name: str
    def __repr__(self) -> str:
        return f"{self.name}({self.arg})"


Node = Union[NumberNode, AddNode, SubstractNode, MultiplyNode, DivideNode, PlusNode, MinusNode, FunctionNode, PowerNode, None]
# TODO: Add Node type for None values?
