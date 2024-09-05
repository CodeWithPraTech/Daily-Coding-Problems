class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ls = []

        lenm = len(rolls)
        total = lenm + n
        all_sum = total*mean
        sum_of_rolls = 0
        for i in rolls:
            sum_of_rolls += i
        diff = all_sum - sum_of_rolls
        mod_of_sum = diff % n
        ele = diff // n
        for i in range(n):
            ls.append(ele)
        i = 0
        while mod_of_sum != 0:
            ls[i] +=1
            i += 1
            mod_of_sum -= 1
        
        for i in ls:
            if i > 6 or i<= 0:
                return []
        
        return ls

        
