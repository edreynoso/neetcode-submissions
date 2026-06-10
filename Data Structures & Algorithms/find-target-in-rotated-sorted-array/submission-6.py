class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 1:
            return -1

        l = 0 
        r = len(nums) -1
        m = 0

        while l <= r:
            m = (l+r) //2
            print(f"Start {l, m,r}")
            if nums[m] == target:
               return m
            elif nums[m] < nums[r]:
                #if m is less than r then everything from r to m is sorted
                if nums[m] < target and target <= nums[r]:
                    print("Search the sorted right half")
                    l = m +1
                else:
                    r = m -1
            else:
                #if m is greater than r then l to m is sorted
                if nums[m] > target and target >= nums[l]:
                    print("Search the sorted left half")
                    r = m-1
                else:
                    l = m +1

        print(nums[m])
        if nums[m] == target:
            return m
        else:
            return -1