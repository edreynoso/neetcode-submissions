class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m -1
        k = n -1

        inv = m + n - 1
        iCount = 0

        while (k >= 0):

            print(nums1, nums1[i],nums2[k], inv)
            if i < 0 and k >= 0:
                
                nums1[k] = nums2[k]
                
                k -=1
            elif nums1[i] <= nums2[k] and i >= 0:
                nums1[inv] = nums2[k]
                k -=1
                inv -=1    
            else:
                nums1[inv] = nums1[i]
                inv -=1
                i -=1
            
            
            




            
                