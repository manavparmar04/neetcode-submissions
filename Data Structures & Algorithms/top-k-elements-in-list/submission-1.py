from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        sorted_count_list = list(sorted_count.keys())
        result = []

        for i in range(k):
            result.append(sorted_count_list[i])

        print(count.keys())
        return result






        '''
        
        eg: [1,1,9,9,9,9,2,2,2]
            {1:2, 9:4, 2:3}

            sorting based on frequenies:
            [9,2,1]

            iterate through k and append values
        
        
        '''