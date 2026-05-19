class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Logic is very simple you need to check the  
        # We have given the integer array [nums[i], nums[j], nums[k]]  
        # All are having the unique indices 
        # Where over here is condition nums[i] + nums[j] + nums[k] == 0
        # And the triplate should be th distint 
        # Brute force method
        # V.1.0
        # First take the result 
        # First loop i until n
        # Second loop j form i+1 till n 
        # third loop k form j+1 till n 
        # at the end if condition check the weather its true false for the condition nums[i] + nums[j] + nums[k] == 0
        # n = len(nums)
        # result = []

        # for i in range(n):
        #     for j in range(i+1 , n):
        #         for k in range(j+1 , n) :
        #             # then check the condition 
        #             sum = nums[i] + nums[j] + nums[k] 
        #             # If condition
        #             if sum == 0 :
        #                 triplet = sorted([nums[i],nums[j],nums[k]])
        #                 if triplet not in result :
        #                     result.append(triplet)
        # return result 

        # V.2.0
        # class Solution:
        # nums = [-1,0,1,2,-1,-4] -> sorted array -> [-4,-1,-1,0,1,2]
                                                      # i L        R 
        nums.sort()
        result = []
        n = len(nums)

        # for loop for the i taking 
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1] :
                continue 
            # this how we can remove the duplicates 
            # then after we need to incremating left & right 
            left = i + 1 
            right = n - 1 

            # while loop when left < right 
            while left < right :
                # formula for the total 
                total = nums[i] + nums[left] + nums[right]
                # total of the number is always zero 
                if total == 0 :
                    # Append the values to the result 
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])
                    
                    # Then move the things forwords left ++ and right --
                    left += 1 
                    right -= 1

                    # condition checkup if the left number is duplicate move left forward
                    while left < right and nums[left] == nums[left - 1] :
                        left += 1
                    # condition checkup for the right number is duplicate move right backword
                    while left < right and nums[right] == nums[right + 1] :
                        right -= 1

                elif total < 0 :
                    left += 1
                
                else :
                    right -= 1

        return result 


