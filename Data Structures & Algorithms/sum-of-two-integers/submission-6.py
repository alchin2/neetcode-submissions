class Solution:
    def getSum(self, a: int, b: int) -> int:
        WIDTH = 12 
        
        def pow2(n: int) -> int:
            p = 1
            for _ in range(n):
                p *= 2
            return p
        
        TWO_POW_W = pow2(WIDTH)

        def to_binary(num: int):
            if num < 0:
                num = TWO_POW_W + num  
            binary = []
            for _ in range(WIDTH):
                binary.append(num % 2)
                num //= 2
            return binary  

        def binary_to(binList):
            val = 0
            power = 1
            for bit in binList:
                val += bit * power
                power *= 2

            if binList[-1] == 1:  
                return val - TWO_POW_W
            return val

        bina = to_binary(a)
        binb = to_binary(b)
        carry = 0
        binc = []

        for i in range(WIDTH):
            d = bina[i] + binb[i] + carry
            binc.append(d % 2)
            carry = d // 2

        return binary_to(binc)
