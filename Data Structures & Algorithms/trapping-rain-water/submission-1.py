
class Solution:
    def trap(self, height: List[int]) -> int:
        # Water Traped at the every index -> we have to find and check 
        # brute force method 
        # V.1.0
        # find the tallest height to the left and to the right 
        # Compute heights
        # Water trap is depends on the left tallest and right tallest wall 
        # Brute force method and why its slow coz it will check the all element again and again 
        
        # n is the lenght of the array
        # n = len(height)
        # # Then Total water 
        # total_water = 0 
        # # then for loop for the range check every index
        # for i  in range(n):
        #     # left_mx and right_mx
        #     left_mx = 0 
        #     right_mx = 0
        #     # To find the left max
        #     for j in range(i):
        #         left_mx = max( left_mx , height[j])
        #     # To find the Right max 
        #     for j in range(i+1 , n):
        #         right_mx = max(right_mx , height[j])
        #     # To find the water as per the fomula 
        #     total_water_is = min(left_mx, right_mx) - height[i]

        #     # condition only positive number we want to get added 
        #     if total_water_is > 0 :
        #         total_water += total_water_is

        # return total_water

        # V.2.0 
        # always depends on the left < right and height 

        n = len(height)

        if not height :
            return 0 

        # then take left and right value 

        left = 0 
        right = n - 1 

        left_max = height[left]
        right_max = height[right]
        
        total_water = 0 

        # then while loop for the left < right 

        while left < right :

            # if loop to check left is samller or larger and move it 
            if left_max < right_max :

                left += 1 

                # Then the left_max = depends on the left value to the water traped 
                left_max = max(left_max , height[left])

                trapped_water = left_max - height[left]

                total_water += trapped_water 
                 
            else :
                right -= 1

                right_max = max(right_max , height[right])

                trapped_water = right_max - height[right]

                total_water += trapped_water
        
        return total_water 























