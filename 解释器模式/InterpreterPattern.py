"""
解释器模式
    给定一个语言，定义它的文法表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

role
    1. 表达式（Expression）
        定义一个接口，用于解释一个上下文。
    2. 终结符表达式（Terminal Expression）
        实现表达式接口，对终结符进行解释。
    3. 非终结符表达式（Non-terminal Expression）
        实现表达式接口，对非终结符进行解释。
    4. 上下文（Context）
        包含解释器需要的全局信息。
"""


"""
context = {
    "a": True,
    "b": False
}
对于这个形式的上下文进行解释，a AND (NOT b) 为 True
"""

from typing import Protocol, Dict

class Expression(Protocol):
    def interpret(self, context: Dict[str, bool]) -> bool:
        ...

# 终结符表达式  表示变量
class VariableExpression:
    def __init__(self, name: str):
        self.name = name

    def interpret(self, context: Dict[str, bool]) -> bool:
        return context.get(self.name, False)

class AndExpression:
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: Dict[str, bool]) -> bool:
        return self.left.interpret(context) and self.right.interpret(context)
    
class OrExpression:
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: Dict[str, bool]) -> bool:
        return self.left.interpret(context) or self.right.interpret(context)

class NotExpression:
    def __init__(self, expr: Expression):
        self.expr = expr

    def interpret(self, context: Dict[str, bool]) -> bool:
        return not self.expr.interpret(context)


if __name__ == "__main__":
    a = VariableExpression("a")
    b = VariableExpression("b")

    # a AND (NOT b)
    rule: Expression = AndExpression(a, NotExpression(b))

    context = {
        "a": True,
        "b": False
    }

    print(rule.interpret(context))  # True


