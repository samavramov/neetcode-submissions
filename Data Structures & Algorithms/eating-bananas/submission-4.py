class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = 0
        while left <= right:
            ktemp = left + (right-left)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/ktemp)
            if total_hours <= h:
                k = ktemp
                right = ktemp -1
            else:
                left = ktemp +1
        return k
            


        