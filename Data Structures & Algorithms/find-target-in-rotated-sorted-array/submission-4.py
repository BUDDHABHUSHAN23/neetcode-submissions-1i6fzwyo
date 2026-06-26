class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # V.1.0
        # For loop for the each index comparing with the targeted element
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i 
        # return -1 

        # V.2.0 -> One Pass method
        # More optimised using the binaery search 
        # Piot -> the index of the smallest element this tell us where is location got mapped
        # [4,5,6,7,0,1,2].
        
        left , right = 0 , len(nums) - 1 

        # Then while loop for the binary search 
        while left <= right :
            # get the mid element 
            mid = (left + right ) // 2
            if nums[mid] == target :
                return mid 
            # then the condition for binary search 
            if nums[left] <= nums[mid] :
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1 
                else : 
                    right = mid - 1
            else :
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1 
                else :
                    left = mid + 1
        return -1 


        
