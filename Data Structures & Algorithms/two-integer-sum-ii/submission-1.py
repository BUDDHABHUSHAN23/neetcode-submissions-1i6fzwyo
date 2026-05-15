class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force method 
        # V.1.0
        # there we will compare the each and every number with another number 
        # like 2 loop -> comparing there sum with the target value 
        # it hit is found then return the ans otherwise return the false
        
        # n = len(numbers)

        # for i in range(n):

        #     for j in range(i+1 , n):

        #         if numbers[i] + numbers[j] == target :

        #             return[i+1 , j+1]   # This is for the outputing purpuse -> not with fuction 

        # V.2.0 
        # This is the optimised output
        # As you see the things array is sorted and we just need to think in the way 
        # where all the smaller number are at  left side and larger number are at right side 
        # formula for the logic is 
        # traget_value = current_sum 
        # current_sum = number[i] + number[j] 
        # case 1: if the sum matches -> ture -> will be the bestcase
        # case 2: if current_sum > target_value -> shift the j towords left side right[::-1]
        # case 3: if the current_sum < target_value -> shidt the i towords right side left[::1]

        # two pointers method 
        left = 0 
        right = len(numbers) - 1 

        # while loop runs until we get the true value 
        while left < right :
            # logic formula for the current sum 
            current_sum = numbers[left]+numbers[right]
            # if and else condition 
            if current_sum == target :
                return[left+1, right+1]
            elif current_sum > target:
                right -= 1
            else :
                left += 1
            













 