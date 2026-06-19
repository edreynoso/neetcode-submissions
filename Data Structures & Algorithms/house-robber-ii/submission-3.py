class Solution:

    def help(self, nums):
        n = len(nums)

        if n == 0 :
            return 0
        if n ==1:
            return nums[0]

        dp = [0] * n
 
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):

            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            

        return dp[-1]

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        return max(self.help(nums[1:]), self.help(nums[:-1]))
        
        