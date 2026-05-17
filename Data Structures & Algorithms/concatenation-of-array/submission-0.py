class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        rlist = nums
        for i in range(len(nums)):
            rlist.append(nums[i])
        return rlist