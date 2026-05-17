class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0

        while l<r:
            curr = (r-l)*min(heights[r],heights[l])
            res = max(res,curr)

            if heights[r]>heights[l]:
                l+=1
            elif heights[r]<=heights[l]:
                r-=1
        
        return res