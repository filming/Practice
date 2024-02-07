from typing import *

# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

''' Notes

'''

''' Complexities 

Solution #1
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    # Solution 1
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # dealing with the case where n is sent in as 0
        if n == 0:
            return True

        # dealing with the case that there's only 1 flowerbed
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
        
        for i in range (len(flowerbed)):
            # handling the cases where the index is pointing at the first/last flowerbed
            if i == 0:
                if (flowerbed[i] == 0) and (flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
            
            if i == (len(flowerbed)-1):
                if (flowerbed[i] == 0) and (flowerbed[i - 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
            
            # handling the cases for the other flowerbeds
            if (flowerbed[i] == 0) and (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            
        # returning a boolean based on the value of n after the loop exists
        if n <= 0:
            return True

        return False

def main():
    solution = Solution()

    flowerbed = [1,0,0,0,1]
    n = 1
    print(solution.canPlaceFlowers(flowerbed, n)) # true

    flowerbed = [1,0,0,0,1]
    n = 2
    print(solution.canPlaceFlowers(flowerbed, n)) # false

if __name__ == "__main__":
    main()