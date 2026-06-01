class Solution:
    def isValid(self, s: str) -> bool:
        # In short this is the on of the example of the finding the opening and closing is the same 
        # Input = "{}" , "{({})}"  => like this way its same and fits the condition 
        # V.1.0
        # Brute force method -> we will do while loop method 
        # if found the "()" with the or condition for the other replace it with the empty string 
        
        while "()" in s or "[]" in s or "{}" in s :
            s = s.replace("()", "")
            s = s.replace("{}","")
            s = s.replace("[]","")

        return s == ""     #This how we can get the solution 
        