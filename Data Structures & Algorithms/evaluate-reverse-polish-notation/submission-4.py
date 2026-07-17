class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        tokens = [int(i) if i not in "+-*/" else i for i in tokens]
        for i in tokens:
            if str(i) not in "+-*/":
                stack.append(i)
                continue
            if i == "+":
                stack = stack[:-2] + [stack[-2] + stack[-1]]
            if i == "-":
                stack = stack[:-2] + [stack[-2] - stack[-1]]
            if i == "*":
                stack = stack[:-2] + [stack[-2] * stack[-1]]
            if i == "/":
                stack = stack[:-2] + [int(stack[-2] / stack[-1])]
        return stack[0]