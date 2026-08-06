class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            p = 1
            for c in str(x):
                p *= int(c)
            return p
        
        num = n
        while digit_product(num) % t != 0:
            num += 1
        return num