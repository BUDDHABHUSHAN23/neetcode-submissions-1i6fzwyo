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
    
        nums.sort()
        result = []

        n = len(nums)

        for i in range(n):

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result
                        