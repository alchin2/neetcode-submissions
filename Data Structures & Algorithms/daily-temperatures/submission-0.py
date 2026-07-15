class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        result = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                curr = stack.pop()
                result[curr[1]] = i - curr[1]
            stack.append((t,i))
        return result