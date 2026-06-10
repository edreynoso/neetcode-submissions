class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx = []

        diff = {}

        for j in range(len(nums)):
            diff[nums[j]] = j

        print(diff)

        for i in range(len(nums)):
            k = target - nums[i]
            if k in diff:
                if diff.get(k) != i:
                    return [i, diff.get(k)]
        