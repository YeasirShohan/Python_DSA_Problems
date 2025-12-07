class Solution:
    def countOdds(low: int, high: int):
        count = 0
        for i in range(low,high+1):
            if i%2==0:
                pass
            else:
                count+=1
        return count