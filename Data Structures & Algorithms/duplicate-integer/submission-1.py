class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for i in range(0,len(nums)):
            if nums[i] in visited:
                return True

            visited.append(nums[i])
        return False