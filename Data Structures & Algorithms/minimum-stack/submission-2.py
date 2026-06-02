class MinStack:

    # Here we have to create the class 
    # With the opreation are like -> push() , pop() , top() , getMin() -> will give the minimum element 
    # Then the opreations are like 
    # push(1)
    # push(2)
    # push(3)
    # then check the getmin() -> 1 
    # pop() -> the top most one 
    # Again get he getMin() 
    # stack    = [5,2,8,1]
    # minStack = [5,2,2,1]
    # As using this we did not need to calculate the min element which is stored

    # V.1.0
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # for the appending the element in the stack 
        self.stack.append(val)

    def pop(self) -> None:
        # for removing the top most element from the stack
        self.stack.pop()
        

    def top(self) -> int:
        # for getting the top most element fo the stack 
        return self.stack[-1]

    def getMin(self) -> int:
        # get the smallest element form the stack
            # create temp list 
            # Pop all element form the stack while tracking smallest val 
            # push all element back from the temp list to restore the stack 
            # return the smallest value found
        return min(self.stack)

    

            

        
