class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # This is not correct and not working properly not properly concatinating 
        # nums add up the entire array and num only addd the 
        # result = []
        # # there will be two for loop 
        # for num in nums:
        #     result.append(nums)
        # for num in nums :
        #     result.append(nums)
        # return result

        # This is the 2 nd with no - index 
        #return nums + nums 

        # With the index based
        n = len(nums)
        result = [0]*(2*n)
        for i in range(n):
            result[i]=nums[i]
            result[i+n]=nums[i]
        return result