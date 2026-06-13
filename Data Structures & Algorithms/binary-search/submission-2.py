class Solution:
    # def search(self, nums: List[int], target: int) -> int:
        # As we know that Binary search is used for the recursive dived and check for the target values 
        # left or right part of the sub-Arrays 
        # If target at the Midel return the index
        # If target larger -> check in right sub-array
        # If target small -> then check in left sub-array
        # simple machanisum -> sort the array -> divide and check unitil get the target value 
        # V.1.0 -> Iterative Binarey search 
        # l , r = 0 , len(nums)-1 
        # while l <= r :
        #     m = l + (r - l) // 2    # for the interger flow its safer to use for bigger number l = 0 and r - 9
        #                             #  0 + 9 // 2  
        #     if nums[m] > target :
        #         r = m - 1 
        #     elif nums[m] < target :
        #         l = m + 1
        #     else :
        #         return m 
        # # if in case target value is not there return - 1
        # return -1 

        # V.2.0 Recursive function 
    def binary_search(self , l : int , r : int , nums:list[int], target : int ) -> int :
        # This apporch is used for the breaking down the task in subtask 
        # like you hire driver -> 
        # driver hires another driver 
        # another driver hires another one driver 
        # l , r = 0 , len(nums) - 1
        if l > r :
            return -1 
    
        # calculate the middle value 
        m = l + (r - l) // 2 

        # check the m and target are same 
        if nums[m] == target :
            return m 
        if nums[m] > target :
            # means its lies in more towords the end side we have to look in the left side reduce r 
            return self.binary_search(l , m-1 , nums , target)
        
        # opposite of above 
        return self.binary_search(m+ 1 , r , nums , target)
    # This is the solution attribute 
    def search(self , nums: list[int] , target : int ) -> int :
        return self.binary_search(0 , len(nums)-1 , nums , target) 
    


        