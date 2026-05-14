class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force method 
        # V.1.0
        # For every number check the next number exist or not 
        # Then next
        # Then next 
        # diff between them is  1 
        #  nums = [1,2,3,4,5]
        
        longest = 0

        for num in nums :
            current_num = num 
            current_length = 1

            while current_num + 1 in nums :
                current_num += 1
                current_length += 1 

            # Here we will need the 

            longest = max(longest , current_length)

            # easy alternative for the above line 

            # if current_length > longest :
            #     longest = current_length

        return longest
