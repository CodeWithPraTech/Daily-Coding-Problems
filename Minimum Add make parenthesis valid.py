class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif len(stack) != 0 and stack[len(stack)-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)

        return len(stack)
        
