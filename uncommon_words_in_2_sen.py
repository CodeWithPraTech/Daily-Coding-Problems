class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a = s1.split(' ')
        b = s2.split(' ')

        c = a
        for i in b:
            c.append(i)
            
        d1 = dict()
        for i in c:
            if i in d1.keys():
                d1[i] += 1
            else:
                d1[i] = 1
        
        res = []
        for i in c:
            if d1[i] == 1:
                res.append(i)

        return res

        
