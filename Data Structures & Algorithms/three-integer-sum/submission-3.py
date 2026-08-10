class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        for i in range(0, len(nums)-1):
            left, right = i, len(nums)-1

            while left < right:
            # ensure distinct indices
                if i == left:
                    left+=1
                    continue

                if i == right:
                    right-=1
                    continue

                is_zero = nums[i] + nums[left] + nums[right]

                if is_zero == 0:
                    res.add((nums[i], nums[left], nums[right]))  
                    left+=1
                    right-=1
                    

                elif is_zero < 0:
                    left+=1
                elif is_zero > 0:
                    right-=1
                    
        return [list(triplet) for triplet in res]
