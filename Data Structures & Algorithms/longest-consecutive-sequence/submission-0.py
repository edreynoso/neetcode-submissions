class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        exist = {}

        for num in nums:

            exist[num] = True

        
        max_x = 0
        
        for num in nums:

            if num-1 not in exist:
                
                count = 1

                while num + count in exist:
                    count +=1
                
                max_x = max(max_x, count)
        
        return max_x
                    




        
