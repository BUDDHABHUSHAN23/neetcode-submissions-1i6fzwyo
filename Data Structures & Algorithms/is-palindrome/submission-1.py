class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The basic work we do that string or num is same as the real one in the reverse
        # so we do have to check for the string removing the spaces and commas or only all usefull char
        # then use the reverse funtion which is build in function in python 
        # then compair resvers and orginal 
        # V.1.0
        # cleaned = ""

        # # traverse throught the each char

        # for ch in s :
             
        #     #  cleanup the string or to keep the all num and char only 

        #     if ch.isalnum():

        #         # convet to the lowercase & convert 

        #         cleaned += ch.lower()

        #     # this is call array slicing[start : stop : steps]
        #     reverse_string = cleaned[::-1]  

        # # compare that they are same or not 

        # return cleaned == reverse_string
 
        # Optimised 
        # V.2.0
        # for the optimised working we wil use the two pointer in the while loop
        # F == L char letter
        # like that two pointers will move
        # if all good contiue the traversing on the array 
        # for the left pointer

        left = 0 
        # Right Pointer
        right = len(s) - 1
        # Here will be the while loop with checking its true or not 
        while left < right :

            # Another while loop 
            while left < right and not s[left].isalnum():
                left += 1   # ----> this direction this will move

            # Another whiile loop 
            while left < right and not s[right].isalnum():
                right -= 1  # <---- this direction this will move 

            # compare the both values & and must be lowein case 
            if s[left].lower() != s[right].lower():
                return False 

        
            # Move inword
            left += 1
            right -=1 

        return True

        