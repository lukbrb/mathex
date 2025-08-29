from mathex.nodes import *
from mathex.values import Number


class Interpreter:
    def visit(self, node: Node, context: dict) -> float:
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node, context)
    
    def visit_NumberNode(self, node: Number, context: dict) -> float:
        return Number(node.value)
    
    def visit_AddNode(self, node: AddNode, context: dict) -> float:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        return Number(left.value + right.value)

    def visit_MinusNode(self, node: MinusNode, context: dict) -> float:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        return Number(left.value - right.value)

    def visit_MultiplyNode(self, node: MultiplyNode, context: dict) -> float:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        return Number(left.value * right.value)
    
    def visit_DivideNode(self, node: DivideNode, context: dict) -> float:
        left = self.visit(node.left, context)
        right = self.visit(node.right, context)
        if right.value == 0:
            raise Exception("Division by zero")
        return Number(left.value / right.value)
    
    def visit_PlusNode(self, node: PlusNode, context: dict) -> float:
        value = self.visit(node.node, context)
        return Number(+value.value)
    
    def visit_MinusNode(self, node: MinusNode, context: dict) -> float:
        value = self.visit(node.node, context)
        return Number(-value.value)
    