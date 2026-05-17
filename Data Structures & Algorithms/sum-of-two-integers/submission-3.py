class Solution:
    def getSum(self, a: int, b: int) -> int:
        WIDTH = 12  # covers sums in [-2000, 2000]
        
        def pow2(n: int) -> int:
            p = 1
            for _ in range(n):
                p *= 2
            return p
        
        TWO_POW_W = pow2(WIDTH)

        def to_binary(num: int):
            """
            Two's-complement little-endian list of length WIDTH.
            """
            # Map negative to unsigned two's-complement value
            if num < 0:
                num = TWO_POW_W + num  # works because num >= -2048 and WIDTH=12
            binary = []
            for _ in range(WIDTH):
                binary.append(num % 2)
                num //= 2
            return binary  # length exactly WIDTH

        def binary_to(binList):
            """
            Convert WIDTH-bit two's-complement little-endian list to signed int.
            No bit shifts used.
            """
            # unsigned value
            val = 0
            power = 1
            for bit in binList:
                val += bit * power
                power *= 2

            # If sign bit (MSB) is 1, subtract 2^WIDTH
            if binList[-1] == 1:  # MSB in little-endian is the last element
                return val - TWO_POW_W
            return val

        bina = to_binary(a)
        binb = to_binary(b)
        carry = 0
        binc = []

        # Fixed-width addition with carry (drop overflow beyond WIDTH)
        for i in range(WIDTH):
            d = bina[i] + binb[i] + carry
            binc.append(d % 2)
            carry = d // 2

        # Ignore final carry (wrap within WIDTH bits)
        return binary_to(binc)
