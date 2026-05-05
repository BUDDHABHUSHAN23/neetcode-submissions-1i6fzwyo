class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Check the frequency map  -> This will have the O(n) 
        count = defaultdict(int)
        for n in nums:
            count[n] += 1 
        # Bucket[i] = list -> the number with frequency count i
        freq = [[] for _ in range(len(nums)+ 1)]
        for num , cnt in count.items():
            freq[cnt].append(num)
        # Scan Right -> left , collect K results *
        result = []
        for i in range(len(freq) -1 , 0 , -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result 


