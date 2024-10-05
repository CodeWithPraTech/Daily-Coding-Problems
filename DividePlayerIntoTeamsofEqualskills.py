class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2:
            return -1
        
        skill = sorted(skill)
        lo , hi = 0 , len(skill)-1

        jt = skill[lo] + skill[hi]

        res = skill[lo] * skill[hi]

        lo, hi = lo + 1, hi - 1

        while lo < hi:
            if skill[lo] + skill[hi] != jt:
                return -1
            if skill[lo] + skill[hi] == jt:
                res += skill[lo] * skill[hi]
                lo += 1
                hi -= 1
        
        return res




