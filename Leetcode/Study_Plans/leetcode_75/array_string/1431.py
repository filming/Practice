from typing import *

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

'''notes
'''

'''approach
Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        # find the largest amount of candies before considering extraCandies
        largest_candies = 0

        for curr_candies in candies:
            if curr_candies > largest_candies:
                largest_candies = curr_candies
        
        # now reiterate over candies, add extraCandies to each one and see if its equal to or greater than the largest_candies found earlier
        for curr_candies in candies:
            if (curr_candies + extraCandies) >= largest_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

def main():
    solution = Solution()

    candies = [2,3,5,1,3]
    extraCandies = 3
    print(solution.kidsWithCandies(candies, extraCandies)) # [true,true,true,false,true] 

    candies = [4,2,1,1,2]
    extraCandies = 1
    print(solution.kidsWithCandies(candies, extraCandies)) # [true,false,false,false,false] 

    candies = [12,1,12]
    extraCandies = 10
    print(solution.kidsWithCandies(candies, extraCandies)) # [true,false,true]

if __name__ == "__main__":
    main()