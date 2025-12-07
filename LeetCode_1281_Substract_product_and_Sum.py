class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summ = 0
        for i in str(n):
            j=int(i)
            product*=j
            summ+=j
        return product - summ