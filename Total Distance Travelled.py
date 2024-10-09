class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        total = 0
        while mainTank != 0:
            if mainTank >= 5:
                mainTank = mainTank - 5

                total += 5*10
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1
            else:
                total += mainTank * 10
                mainTank = 0

        return total
    


