class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n *n
        sumEven = n * (n + 1)
        
        while sumEven:
            sumOdd, sumEven = sumEven, sumOdd % sumEven
        
        return sumOdd