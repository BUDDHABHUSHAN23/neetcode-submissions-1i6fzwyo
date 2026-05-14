class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force method 
        # V.1.0
        # For every number check the next number exist or not 
        # Then next
        # Then next 
        # diff between them is  1 
        #  nums = [1,2,3,4,5]
        
        # longest = 0

        # for num in nums :
        #     current_num = num 
        #     current_length = 1

        #     while current_num + 1 in nums :
        #         current_num += 1
        #         current_length += 1 

        #     # Here we will need the 

        #     longest = max(longest , current_length)

        #     # easy alternative for the above line 

        #     # if current_length > longest :
        #     #     longest = current_length

        # return longest

        # V.2.0 
        # This will be the more optimised output where we will first convert the list into set 
        # set is best for the lookup with time complexity is O(1) to check num+1 & num-1
        # then process will be loop goes through every element 
        # first checking the num-1 is if its not there put it is as the start 
        # Then check for the num+1 and go arround untile it breaks 
        # for the 2 num in the set and then check num-1 if its exist then skip the checking 
        # this is how the optimised way should work 

        # first convert the list into set

        new_set = set(nums)

        longest = 0 

        for num in new_set :

            # check its start or not 

            if (num - 1 ) not in new_set :

                # Then the length assign = 1

                length = 1

                # Then while loop for the iteration for (num + 1)

                while (num + length) in new_set :

                        length += 1 


                longest = max(longest , length)


        return longest

















