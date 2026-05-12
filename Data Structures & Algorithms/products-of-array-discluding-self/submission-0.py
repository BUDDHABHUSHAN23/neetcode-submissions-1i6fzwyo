class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Burtforce method ->
        # Outer loop traversing through every element 
        # Innner loop doing the mutiplication with other element expect other 
        # Then finally we will get the output num array 
        #  v.1.0
        #         result = []

        # # outer loop for the all element in the array 
        # #  This goes through the all elements over there
        # for i in range(len(nums)) :
        #     product = 1 
        #     # inner loop but condition is that except itself 
        #     for j in range(len(nums)):
        #         # except itself -> this condition 
        #         if i != j :
        #             product *= nums[j]

        #     result.append(product)

        # return result

        # Optimised method 
        # Prefix Product - Product of the all element before index
        # Sufix Product - Product of the all element after index

        # v.2.0
        # this will be the length of the nums
        n = len(nums)
        # Initialize the Prefix , sufix , result 
        prefix = [1] * n
        sufix  = [1] * n
        result = [1] * n 

        # Build the perfix array
        for i in range(1 , n) :
            prefix[i] = prefix[i - 1]*nums[i - 1]

        for i in range(n-2 , -1 , -1): # if n  = 4 -> start form 2 position -> stops at -1 , steps => +1
            sufix[i] = sufix[i+1]*nums[i+1]

        for i in range(n):
            result[i] = prefix[i]*sufix[i]

        return result














