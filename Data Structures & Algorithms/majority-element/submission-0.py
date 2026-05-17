class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for n in nums:
            if n not in count_dict:
                count_dict[n] = 1
            else:
                count_dict[n]+=1
        res = max(count_dict, key=count_dict.get)
        return res