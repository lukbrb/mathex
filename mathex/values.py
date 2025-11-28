from dataclasses import dataclass
from typing import Callable

fn_type = Callable[[float], float]
@dataclass
class Number(float):
    value: float
    def __repr__(self) -> str:
        return f"{self.value}"
    
@dataclass
class Function:
    # So far functions are assumed to be pure math functions with a single argument
    name: str
    arg: Number
    implementation: fn_type
    def __repr__(self) -> str:
        return f"{self.name}({self.arg})"
    
    def evaluate(self) -> Number:
        res = self.implementation(self.arg.value)
        return Number(res)
