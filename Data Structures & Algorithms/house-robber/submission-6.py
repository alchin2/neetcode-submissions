class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
                 
        n = len(nums)
        dp = [0] * (n + 1) 
         
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
         
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 
        # at each house i:
        # case 1 rob: dp[i-2] + nums[i]
        # case 2 dont rob: dp[i-1]
        return dp[n-1]
