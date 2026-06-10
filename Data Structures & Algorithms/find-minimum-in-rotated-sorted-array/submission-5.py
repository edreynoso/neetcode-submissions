class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) -1 

        if len(nums) == 1:
            return nums[0]

        m = 0
        while l < r:
            m = (l+r) //2

            if nums[m] <= nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m +1
        
        if nums[m] <= nums[r]:
            return nums[m]
        else:
            return nums[m+1]

