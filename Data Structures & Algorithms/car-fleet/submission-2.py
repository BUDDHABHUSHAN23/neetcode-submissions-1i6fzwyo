class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We have to consider that there are n number of cars traveling on the one-lane-highway
        # we have given the two array 
            # Position -> Will show the position of ith car in -> mile unit 
            # Speed    -> Will show speed of ith car -> miles per hr unit
        # Destination is the target position in miles 
        # Car can not take over to each other 
        pairs = [(p , s )  for p ,s in zip(position , speed)]
        pairs.sort(reverse=True)
        stack = []
        for p,s in pairs :
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2] :
                stack.pop()
        return len(stack)