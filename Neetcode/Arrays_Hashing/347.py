from typing import *

# https://leetcode.com/problems/top-k-frequent-elements/

'''notes
'''

'''approach
Solution #1
Time Complexity: O(N log N)
Space Complexity: O(N)

Solution #2
Time Complexity: O(N)
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

    # Solution 2
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        num_occurrences = {}

        # get the occurrences of each num in nums
        for curr_num in nums:
            if curr_num in num_occurrences:
                num_occurrences[curr_num] += 1
            else:
                num_occurrences[curr_num] = 1
        
        # use bucket sorting to sort the occurrences from least to greatest
        num_occurrences_buckets = [[] for _ in range (len(nums))] # a new list obj must be created at each index, using [[]] * x, does not create x new lists but just copies one over

        for no_k,no_v in num_occurrences.items():
            num_occurrences_buckets[no_v-1].append(no_k)

        # get the last k elements and add it to result, these are our top k frequent elements
        for i in range (len(num_occurrences_buckets)-1, -1, -1): # iterate over each bucket, starting from the last bucket
            for j in range (len(num_occurrences_buckets[i])): # iterate over each element in the current bucket
                if len(result) == k:
                    break
                
                result.append(num_occurrences_buckets[i][j])
        
        return result

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