from typing import *

# https://leetcode.com/problems/two-sum/

'''notes
'''

'''approach
Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indexes = {}

        for i in range (len(nums)):
            difference = target - nums[i]

            if difference in num_indexes:
                return [num_indexes[difference], i]

            else:
                num_indexes[nums[i]] = i
        
        return [-1, -1]


def main():
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums, target)) # [0,1]

    nums = [3,2,4]
    target = 6
    print(solution.twoSum(nums, target)) # [1,2]

    nums = [3,3]
    target = 6
    print(solution.twoSum(nums, target)) # [0,1]

if __name__ == "__main__":
    main()