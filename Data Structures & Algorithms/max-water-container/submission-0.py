class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Understanding of the code 
        # Index:    0 1 2 3 4 5 6 7
        # Height:   1 7 2 5 4 7 3 6
        # |               |    => this is for 
        # |               |
        # |       |       |
        # |   |   |   |   |
        # -----------------
        # V.1.0
        # brute force method 
        # Try every pair 
        # Two loops and get the width and height 
        # Get the area -> then find the max sorted
        # n = len(heights)
        # # This is the max_area
        # max_area = 0
        # # for loop
        # for i in range(n):
        #     for j in range(i+1 , n):
        #         # get the width 
        #         width = j - i
        #         # Height 
        #         height = min(heights[i] , heights[j])
        #         # area
        #         area = width * height 
        #         # max_area
        #         max_area = max(max_area , area)
        # return max_area

        # V.2.0
        # more optimised approch
        # use while loop -> with two pointer 

        n = len(heights)
        # left pointer
        left = 0 
        # Right pointer
        right = n - 1
        # Max_area
        Max_area = 0
        # while loop where left< right 
        while left < right :
            # width
            width = right  - left
            # heights 
            Min_height = min(heights[left] , heights[right])
            # Area 
            area = width * Min_height
            # get max value
            Max_area = max(Max_area , area)
            # check the things and shiting of pointer
            if heights[left]<heights[right]:
                left += 1
            else :
                right -= 1
        
        return Max_area
