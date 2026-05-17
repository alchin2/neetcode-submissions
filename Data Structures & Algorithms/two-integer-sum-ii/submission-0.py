class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1


        while left<right:
            res = numbers[right]+numbers[left]
            if res > target:
                right-=1
            if res < target:
                left+=1
            if res == target:
                return [left+1,right+1]

