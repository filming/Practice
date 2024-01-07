from typing import *

# https://leetcode.com/problems/top-k-frequent-elements/

'''notes
'''

'''approach
Solution #1
Time Complexity: O(N log N)
Space Complexity: O(N)
'''

class Solution:
    # Solution 1
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []

        num_occurrences = {}

        # get the occurrences of each num in nums
        for curr_num in nums:
            if curr_num in num_occurrences:
                num_occurrences[curr_num] += 1
            else:
                num_occurrences[curr_num] = 1
        
        num_occurrences_sorted = sorted(num_occurrences.items(), key = lambda x: x[1], reverse = True)

        for i in range(k):
            answer.append(num_occurrences_sorted[i][0])

        return answer

def main():
    solution = Solution()

    nums = [1,1,1,2,2,3]
    k = 2
    print(solution.topKFrequent(nums, k)) # [1,2]

    nums = [1]
    k = 1
    print(solution.topKFrequent(nums, k)) # [1]

if __name__ == "__main__":
    main()