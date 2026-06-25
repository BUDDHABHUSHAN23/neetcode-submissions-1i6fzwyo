class Solution:
    def findMin(self, nums: List[int]) -> int:
        # V.1.0
        # This will be the brute force method 
        # simple way is to look up in the arrya 
        # return min(nums)

        # V.2.0
        # One part will be always sorted & another part contains the rotation 
        # logic using the binary search 
        # if the left part is sorted the check for the minimum element in right 
        # if right part is sorted then check for the minium element in the left 
        
        res = nums[0]
        left , right = 0 , len(nums) - 1 

        # while loop
        while left <= right :
            if nums[left] < nums[right] :
                res = min(res , nums[left])
                break 
            # Then we will compute this 
            mid = (left + right) // 2 
            res  = min(res , nums[mid])
            if nums[mid] >= nums[left]:
                left = mid  + 1
            else :
                right = mid - 1 
        return res
