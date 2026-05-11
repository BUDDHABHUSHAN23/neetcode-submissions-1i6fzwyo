class Solution:
# The main things is that we need the single string without space as a single object  -> we have to work on the list of string
# Remove the empty spaces with the help of replacing # 
# Encoded and decoded string are should be the same



    def encode(self, strs: List[str]) -> str:
    # Here will be the logic for the encoding the string 
        # first result  -> empty string 
        result = ""
        for word in  strs :
            # for contiouse string 
            result += str(len(word)) + "#" + word
            # return the result 
        return result   #"5#Hello5#World"

    def decode(self, s: str) -> List[str]: 
        # Here is the logic for the decoding the string 
        # This decoding part work with the s = "5#Hello5#World"  \
        # we are going to keep the 2 index i & j where  i always start with
        # i where 1 char of the string -> where the current encoding part get start
        # J moves until we get the # inside the inner loop
        # [length]#[word]  -> This is the formate of the word
        #================================================================================

        result = []
        # Put i = 0 
        i = 0 
        # while loop i value is must be less that lenght of whole object string
        while i < len(s) :
            # start searching inside the block 
            # with inner loop i=j
            j = i 
            # interate until it find the "#" in the object string 
            while s[j]  != "#" :
                j += 1   # this will give you the separater
            # get the lenght lenght -> s [i : j ] -> convert into the int
            length = int(s[i:j])  # -> like this way S[0:1] -> will give you int -> 5

            # now we have the lenght separater j we have to use 
            # so that j+1 : j+1+lengh -> will give use the exact length
            word = s[j+1 : j+1+length]

            # then we have to append the word to result 
            result.append(word) 

            # for further word or iteration we need the to move to words the next word

            i = j+1+length # -> this how we can move the i to words the next length and separeter

        return result



         











