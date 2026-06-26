class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # V.1.0
        # For loop for the each index comparing with the targeted element
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
        return -1 