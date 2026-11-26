from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        top_freq = dict(count.most_common())
        ls = list(top_freq.keys())

        result = []

        for i in range(k):
            result.append(ls[i])

        return result
            

