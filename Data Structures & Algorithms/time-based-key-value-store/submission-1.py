class TimeMap:
    # This example is for the key -> values pairs -> with the mutiple values for a single key
    # "alice" → [[1, "happy"], [3, "sad"], [7, "tired"]]
    # set() -> always take the timestamp in the strick increasing order -> so that all array will be sorted as per the timestamp
    # time:  1        3        7
    # value: "happy"  "sad"    "tired"
    # get() ->  To get("alice", 5)  -> timestamp_prev <= timestamp  -> which is the most recent less than equal to 
    # If there is no value -> ""


    def __init__(self):
        # V.1.0
        # creating the dictioney 
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # V.1.0
        # Here we are storing the value with the time
        if key not in self.keyStore:
            self.keyStore[key] = {}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        # V.1.0
        # if the key doesnt exit return empty string 
        if key not in self.keyStore:
            return ""
        
        # store the seen value 
        seen = 0 

        # Check with the condition 
        for time in self.keyStore[key]:
            if time <= timestamp :
                seen = max(seen , time )
        return "" if seen == 0 else self.keyStore[key][seen][-1]