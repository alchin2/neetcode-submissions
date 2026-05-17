class Solution:
    def getSum(self, a: int, b: int) -> int:

        def to_binary(num: int):
            if num < 0:
                num = 4096 + num  
            binary = []
            for _ in range(12):
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
                return val - 4096
            return val

        bina = to_binary(a)
        binb = to_binary(b)
        carry = 0
        binc = []

        for i in range(12):
            d = bina[i] + binb[i] + carry
            binc.append(d % 2)
            carry = d // 2

        return binary_to(binc)
