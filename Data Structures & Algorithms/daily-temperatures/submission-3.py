class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # As per the understanding we have to find the max number 
        # from the current index so that in output we can able to provide the 
        # Difference in that  -> If ther is not any kind of result add 0 
        # Brute Force 
        # V.1.0
        # We need to compare ith element through out the all list or array 
        # And add the diff to the outPut 
        # The complexity will be the O(n^2)

        # Input: temperatures = [30,38,30,36,35,40,28]
        #              Output = [1,4,1,2,1,0,0]
        
        # Get the length first
        # n = len(temperatures)
        # res = [0] * n 

        # # we have to check the all of element of list or array 
        # for i in range(n):
        #     # Here count will be 1 
        #     count = 1
        #     # Here J will be traversing to the next day 
        #     j = i + 1 
        #     # then condition 
        #     while j < n :
        #         if temperatures[j] > temperatures[i] :
        #             break
        #         # Increament the J for the nex number 
        #         j += 1
        #         # Also increment the count 
        #         count += 1

        #     # Then condition to check the count is same as the n 

        # Bit more imporve on 
        # for i in range(n) :
        #     for j in range(i+1 , n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i 
        #             break

        # return res


        # V.1.0
        # We stack helps keep track of days still waiting for the warmer day 
        # Scan forward -> when we finds the greater temp one on the top -> means we have discoverd the next higher temp from the earlier dayy 
        # We pops it & computes the days diff byy doing the i - j 
        # We will use over here is the monotonic stack 
        res = [0]*len(temperatures)
        stack = []  # pair: [temp , index]

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))    
        return res
