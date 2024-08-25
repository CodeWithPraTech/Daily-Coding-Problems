class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(num):
            if  num <= 1:
                return 0
            
            if num == 2:
                return 1
            i = 2
            
            while i < num:
                if num % i == 0:
                    #print(" a")
                    return 0
                i += 1
            return 1
        
        ls = []
        for i in nums:
            ls.append(isPrime(i))

        k, l = 0, len(nums)-1
        while k <= l:
            if ls[k] == 1:
                break
            k = k + 1
        
        while k <= l:
            if ls[l] == 1:
                break
            l = l - 1
        #print(ls)

        return l -k

        