class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force method 
        # V.1.0
        # there we will compare the each and every number with another number 
        # like 2 loop -> comparing there sum with the target value 
        # it hit is found then return the ans otherwise return the false
        
        n = len(numbers)

        for i in range(n):

            for j in range(i+1 , n):

                if numbers[i] + numbers[j] == target :

                    return[i+1 , j+1]

