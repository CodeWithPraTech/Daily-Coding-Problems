class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator = {
            "+": lambda x,y : x+y,
            "*": lambda x,y : x*y,
            "-": lambda x,y : x-y,
        }

        def backtrack(left,right):
            res = []

            for i in range(left,right+1):
                op = expression[i]
                if op in operator:
                    num1 = backtrack(left, i-1)
                    num2 = backtrack(i+1, right)

                    for p in num1:
                        for q in num2:
                            res.append(operator[op](p,q))
                    

            if res == []:
                res.append(int(expression[left:right+1]))
            return res
        
        return backtrack(0,len(expression)-1)
        
