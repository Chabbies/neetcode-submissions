class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #1,7,2,5,4,7,3,6
        greatest_area = 0
        left, right = 0, len(heights)-1
        # left = 0, right = 7

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            greatest_area = max(area, greatest_area)
            #h[left] = 1, h[right] = 7 --> 1*(0-7)
            if heights[left] <= heights[right]:    
                left += 1
            else:
                right -= 1

        return greatest_area
