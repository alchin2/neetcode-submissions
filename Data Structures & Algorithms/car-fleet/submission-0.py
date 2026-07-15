class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [] #(pos, speed)
        for i in range(len(position)):
            comb.append((position[i],speed[i]))

        comb.sort(key=lambda x: x[0], reverse=True)

        stack = [comb[0]]
        for i in range(1, len(comb)):
            p1, s1 = comb[i]
            p2, s2 = stack[-1]

            if s1 <= s2:
                stack.append((p1, s1))
                continue

            meet_pos = p1 + s1 * ((p2 - p1) / (s1 - s2))
            if meet_pos > target:
                stack.append((p1, s1))

        return len(stack)