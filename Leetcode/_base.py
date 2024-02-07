from typing import *

# LINK

''' Notes

'''

''' Complexities 

Solution #1
Time Complexity: 
Space Complexity:
'''


class Solution:
    # Solution 1
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass



def main():
    solution = Solution()

    nums = [1,2,3,1]
    print(solution.containsDuplicate(nums)) # true

    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums)) # false

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(solution.containsDuplicate(nums)) # true

if __name__ == "__main__":
    main()