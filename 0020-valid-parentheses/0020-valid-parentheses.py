class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            "(":")",
            "{":"}",
            "[":"]",
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != i:
                    return False
        return len(stack) == 0

        