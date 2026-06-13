class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # As we know that Binary search is used for the recursive dived and check for the target values 
        # left or right part of the sub-Arrays 
        # If target at the Midel return the index
        # If target larger -> check in right sub-array
        # If target small -> then check in left sub-array
        # simple machanisum -> sort the array -> divide and check unitil get the target value 
        # V.1.0 -> Iterative Binarey search 
        l , r = 0 , len(nums)-1 
        while l <= r :
            m = l + (r - l) // 2    # for the interger flow its safer to use for bigger number l = 0 and r - 9
                                    #  0 + 9 // 2  
            if nums[m] > target :
                r = m - 1 
            elif nums[m] < target :
                l = m + 1
            else :
                return m 
        # if in case target value is not there return - 1
        return -1 


        