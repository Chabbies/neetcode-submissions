class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #index 1 != index 2
        #-5,-3,0,2,4,6,8
        result = []
        left, right = 0, len(numbers) - 1
        # left == 1 --> -5 and right == 7 --> 8

        while right > left:
            #7 > 1 it one
            #2 > 0
            sum = (numbers[right] + numbers[left])

            if sum == target:
                #num @ right 4 + nums @ left 1 == 3 NO it 1
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif sum < target:
                #right == 2 it 1
                left += 1 
            else:
                right -= 1


            
