class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The basic work we do that string or num is same as the real one in the reverse
        # so we do have to check for the string removing the spaces and commas or only all usefull char
        # then use the reverse funtion which is build in function in python 
        # then compair resvers and orginal 

        cleaned = ""

        # traverse throught the each char

        for ch in s :
             
            #  cleanup the string or to keep the all num and char only 

            if ch.isalnum():

                # convet to the lowercase & convert 

                cleaned += ch.lower()

            # this is call array slicing[start : stop : steps]
            reverse_string = cleaned[::-1]  

        # compare that they are same or not 

        return cleaned == reverse_string
 

        