class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for i in range(len(nums)):
            curr = nums[i]
            need = target - curr
            if need in seen:
                left = min(i,seen.get(need))
                right = max(i,seen.get(need))
                return [left,right]
            else:
                seen[curr]=i
        