class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        r = 1

        while (l < len(nums)-1):

            if r <= len(nums)-1:
                if abs(l - r) <= k and nums[l] == nums[r]:
                    return True
                else:
                    r +=1
            else:
                l +=1
                r = l+1
        return False
