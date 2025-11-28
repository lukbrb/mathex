from collections.abc import Callable
from mathex.function import FUNCTIONS
from mathex.nodes import (Node, AddNode, SubstractNode, MultiplyNode,
                          DivideNode, PlusNode, MinusNode, FunctionNode)
from mathex.values import Number


Ctx_Type = dict[str, float]
class Interpreter:
    def visit(self, node: Node, context: Ctx_Type) -> Number:
        method_name: str = f'visit_{type(node).__name__}'
        method: Callable[[Node, Ctx_Type], Number] = getattr(self, method_name)
        return method(node, context)

    def visit_NumberNode(self, node: Number, context: Ctx_Type) -> Number:
        return Number(node.value)

    def visit_AddNode(self, node: AddNode, context: Ctx_Type) -> Number:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        return Number(left.value + right.value)

    def visit_SubstractNode(self, node: SubstractNode, context: Ctx_Type) -> Number:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        return Number(left.value - right.value)

    def visit_MultiplyNode(self, node: MultiplyNode, context: Ctx_Type) -> Number:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        return Number(left.value * right.value)

    def visit_DivideNode(self, node: DivideNode, context: Ctx_Type) -> Number:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        if right.value == 0:
            raise Exception("Division by zero")
        return Number(left.value / right.value)

    def visit_PlusNode(self, node: PlusNode, context: Ctx_Type) -> Number:
        value = self.visit(node.node, context)
        return Number(+value.value)

    def visit_MinusNode(self, node: MinusNode, context: Ctx_Type) -> Number:
        value = self.visit(node.node, context)
        return Number(-value.value)

    def visit_FunctionNode(self, node: FunctionNode, context: Ctx_Type) -> Number:
        arg_value = self.visit(node.arg, context)
        function_impl = FUNCTIONS.get(node.name)
        if function_impl is None:
            raise Exception(f"Unknown function '{node.name}'")
        result = function_impl(arg_value.value)
        return Number(result)
