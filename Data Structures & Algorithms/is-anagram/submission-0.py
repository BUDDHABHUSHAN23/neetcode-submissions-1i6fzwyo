class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Here we can use the counter and 
        return Counter(s) == Counter(t)