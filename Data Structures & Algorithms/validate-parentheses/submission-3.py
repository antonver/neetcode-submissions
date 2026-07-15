class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        for i in s:
            if i in d.keys():
                stack.append(i)
                continue
            if len(stack) > 0:
                start = stack.pop()
                if i == d[start]:
                    continue
            return False
        return len(stack) == 0