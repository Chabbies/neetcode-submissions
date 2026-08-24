class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0,3,2,5,4,6,1,1
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in num_set:
                #is the current num a sequence starter
                #does 0-1 exist in set == no
                length = 0
                while(num + length) in num_set:
                    #0+0 iteration 1
                    #0+1 iteration 2
                    #1+1 iteration 3
                    #1+2 iteration 4
                    length += 1
                    #0,1,2 .... current list
                    #1,2,3 .... Count
                longest = max(length, longest)
        return longest
                
