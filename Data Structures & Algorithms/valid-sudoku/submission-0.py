class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # From the input we are able to know that its list based problem -> or we can call it is as the nested list 
    # or we can use the external lib numpy for the showcasing of the matix
    #   R = 1 , C = 1
    # [["1","2",".",".","3",".",".",".","."],
    #  ["4",".",".","5",".",".",".",".","."],
    #  [".","9","8",".",".",".",".",".","3"],
    #  ["5",".",".",".","6",".",".",".","4"],
    #  [".",".",".","8",".","3",".",".","5"],
    #  ["7",".",".",".","2",".",".",".","6"],
    #  [".",".",".",".",".",".","2",".","."],
    #  [".",".",".","4","1","9",".",".","8"],
    #  [".",".",".",".","8",".",".","7","9"]]
    # Here we understand that every cell contains the number form 1-9 and there should not be any kind of duplicate is present
    # This is the 9*9 matrix / Board in that 9 -> 3*3 -> sub matrix they should contain the numbers form the 1 - 9 

    # V.1.0 -> Brute force -> how should i check the conditions ?
    # 81 cells ->> 9{cols} , 9{rows} , 9{sub martix}
    # So the time complexity will be goes through the every things about n time n*n*n -> n^3 
    # And we have to check that "." -> empty value is not there then compair means there is value only we have to compare 
    # Another things is that while comparing suppose 
    # board[b][c] = 5 -> we have to skip the current index -> otherwise it will check itself and always mark as the duplicate has been found 

    # # Row check code 
    # for col in range(9):
    #     # skip the current place
    #     if col == c :
    #         continue 
    #     if board[r][col] == value :
    #         return false 
    
    # # Col check code 
    # for row in range(9)
    #     # skip the current place 
    #     if row == r :
    #         continue
    #     if board[c][row] == value :
    #         return false 

    # # check for the 3*3 matrix
    # # to find this we need the to find the exact where the elements is present 
    # # Formula we will use that 
    # start_row = (r//3)*3
    # start_col = (c//3)*3

    # for row in range(start_row , start_row+3):
    #     for col in range(start_col , start_col+3):
    #         # Ingnore the current index 
    #         if row == r and col == c :
    #             continue 
    #         # check for the duplicate 
    #         if board[row][col] ==value :
    #             return false 


        for r in range(9):
            for c in range(9):

                #assing the value = board[r][c]
                value = board[r][c]


                #  we have to skip the "."

                if value == ".":
                    continue 
                
                # # Row check code 
                for col in range(9):
                    # skip the current place
                    if col == c :
                        continue 
                    if board[r][col] == value :
                        return False


                # # Col check code 
                for row in range(9):
                    # skip the current place 
                    if row == r :
                        continue
                    if board[row][c] == value :
                        return False 

                # for row in range(start_row , start_row+3):
                
                start_row = (r//3)*3
                start_col = (c//3)*3
    
    
                for row in range(start_row , start_row+3):
                    for col in range(start_col , start_col+3):
                        # Ingnore the current index 
                        if row == r and col == c :
                            continue 
                        # check for the duplicate 
                        if board[row][col] ==value :
                            return False 


        return True



