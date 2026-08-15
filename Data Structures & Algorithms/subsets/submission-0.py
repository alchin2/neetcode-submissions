class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            temp = []
            
            for current_subset in res:
                temp.append(current_subset + [num])
            
            res.extend(temp)
            
        return res
