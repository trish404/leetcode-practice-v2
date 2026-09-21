class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            x = target - nums[i] 
            if x in nums and nums.index(x) != i:
                return [i,nums.index(x)]
        
