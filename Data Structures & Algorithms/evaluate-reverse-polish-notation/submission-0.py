class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # V.1.0 
        # We will use the list for the brute force method 
        # where object is created 
        # While loop will travas through the whole array or list check if it opration 
        # we have to use the 2 different index in array 
        # then operation in the if elif else condition 
        # after all push the result to the list again
        # Token = [1,2,-,3,4,5]

        # This are the operators we are using
        operators = {
             "+",
            "-",
            "*",
            "/"
        }   

        while len(tokens) > 1 :
            for i in range(len(tokens)) :
                if tokens[i] in operators :
                    # We have to get the two number right 
                    # we need the output on the form of token where i is tarversing through the list for the operator 
                    # i = "-"
                    a = int(tokens[i-2]) # Output will be the index 0 = 1
                    b = int(tokens[i-1]) # Output will be the index 1 = 2 
                    if tokens[i] == "+":
                        result = a + b
                    elif tokens[i] == "-":
                        # if b > a :
                        #     result = b - a
                        # else :
                            result = a - b 
                    elif tokens[i] == "*":
                        result = a * b
                    else :
                        result = int(a/b) # this will round of the value and give it in positive outcome 

                    # now token the main part turcate 
                    tokens = (
                        tokens[:i - 2] + [str(result)] + tokens[i+1:]
                    )

                    break

        return int(tokens[0])
                            

        