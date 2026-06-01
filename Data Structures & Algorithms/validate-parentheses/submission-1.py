class Solution:
    def isValid(self, s: str) -> bool:
        # In short this is the on of the example of the finding the opening and closing is the same 
        # Input = "{}" , "{({})}"  => like this way its same and fits the condition 
        # V.1.0
        # Brute force method -> we will do while loop method 
        # if found the "()" with the or condition for the other replace it with the empty string 
        
        # while "()" in s or "[]" in s or "{}" in s :
        #     s = s.replace("()", "")
        #     s = s.replace("{}","")
        #     s = s.replace("[]","")

        # return s == ""     #This how we can get the solution 

        # V.2.0 -> More optimised version 
        # compare both of them and if its match return true or else false 
        # while cross checking the input read -> push in the stack 
        # The comparision is like this way stack 1 top peek and if match pop 
        # At the end you will get the empty array

        # stack 
        stack = []

        # we will map the brakets for the showing which belong to whom
        map_pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        
        }

        for ch in s :
            # fetch the all the char in it 
            if ch in map_pairs :
                # first the map_pair stack -> empty 
                if stack and stack[-1] == map_pairs[ch]:
                    stack.pop()
                else :
                    return False
                
            else :
                stack.append(ch)

        return len(stack) == 0
