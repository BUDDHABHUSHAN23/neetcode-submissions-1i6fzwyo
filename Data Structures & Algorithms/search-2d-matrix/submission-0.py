class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # here is the matrix given to use we have to use it to find target value
        # V.1.0
        # Brute force method 
        # 2 loops on is for the row then int that row -> cols 
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == target :
        #             return True 
        #     return false 

        # V.2.0
        # Optimsied
        # We need to apply for the two binary searchs for that 
        # First search over the row 
        # Then search inside the row 
        # we need the both row and cols 
        
        ROWS , COLS = len(matrix) , len(matrix[0])

        # Now for the top_row and bot_row
        top , bot = 0 , ROWS-1 
        # Then while loop
        while top <= bot :
            row = (top + bot ) // 2  # Which will give use the mid for the row only one the outer layer
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row -1 
            else :
                break 

        # What if the top is not greater than the bot 
        if not (top <= bot) :
            return False

        # Then work on the selected row 

        row = ( top + bot ) // 2
        l , r = 0 , COLS -1 
        while l <= r :
            m = (l + r) // 2
            if target > matrix[row][m] :
                l = m + 1 
            elif target < matrix[row][m] :
                r = m - 1
            else:
                return True
        return False
            
 
