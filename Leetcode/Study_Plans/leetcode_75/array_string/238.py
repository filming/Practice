from typing import *

# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

''' Notes

'''

''' Complexities 

Solution #1
Time Complexity: O(n)
Space Complexity: O(n)

Solution #2
Time Complexity: O(n)
Space Complexity: O(1), since result/answer list doesn't count towards memory calculations
'''


class Solution:
    # Solution 1
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, prefix_products, suffix_products = [0] * len(nums), [0] * len(nums), [0] * len(nums)

        # creating a running-product list going from the left to right elements of nums
        previous_product = 1
        for i in range (len(prefix_products)):
            next_product = previous_product * nums[i]

            prefix_products[i] = next_product
            previous_product = next_product
        
        # creating a running-product list going from the right to left elements of nums
        previous_product = 1
        for i in range (len(suffix_products)-1, -1, -1):
            next_product = previous_product * nums[i]

            suffix_products[i] = next_product
            previous_product = next_product
        
        # use the values in the prefix/suffix lists in order to find the overall product of an array not including a specific index
        for i in range (len(result)):
            # handle cases where prefixes and/or suffix values DO NOT exist adjacent to an index
            if i == 0:
                result[i] = suffix_products[i+1]

            elif i == (len(result)-1):
                result[i] = prefix_products[len(prefix_products)-2]

            # handle cases where prefixes and/or suffix values exist adjacent to an index
            else:
                result[i] = prefix_products[i-1] * suffix_products[i+1]
        
        return result
    
    # Solution 2
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        # setting up our result list to be a running-product list going from the left to right elements of nums
        result[0] = 1
        for i in range(1, len(nums)):
            # result[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            result[i] = nums[i - 1] * result[i - 1]

        # use a variable to store the running-product of the elements from the right to left of nums
        curr_right_product = 1
        for i in range (len(result)-1 , -1, -1):
            result[i] *= curr_right_product

            curr_right_product *= nums[i]
            
        return result

def main():
    solution = Solution()

    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums)) # [24,12,8,6]

    nums = [-1,1,0,-3,3]
    print(solution.productExceptSelf(nums)) # [0,0,9,0,0]

if __name__ == "__main__":
    main()
