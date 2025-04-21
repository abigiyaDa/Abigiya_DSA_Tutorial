class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]!=0 and nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
        while len(res) < len(nums):
            res.append(0)
        
        return res