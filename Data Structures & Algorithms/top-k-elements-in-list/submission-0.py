class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_freq = {}
        for num in nums:
            element_freq[num] = 1 + element_freq.get(num,0) 
        
        sorted_nums = []
        for num, count in element_freq.items():
            sorted_nums.append([count, num])
        sorted_nums.sort()

        result = []
        while len(result) < k:
            result.append(sorted_nums.pop()[1])
        return result

