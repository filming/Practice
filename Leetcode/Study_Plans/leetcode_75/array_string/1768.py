from typing import *

# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

'''notes
'''

'''approach
Solution #1
Time Complexity: O(n)
Space Complexity: O(n+m)
'''

class Solution:
    # Solution 1
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_chars = []

        word1_curr_index, word2_curr_index = 0, 0

        while (word1_curr_index <= (len(word1)-1)) and (word2_curr_index <= (len(word2)-1)):
            merged_chars.append(word1[word1_curr_index])
            merged_chars.append(word2[word2_curr_index])

            word1_curr_index += 1
            word2_curr_index += 1
        
        # add the remaining chars of the word1/word2 string if they exist
        if word1_curr_index <= (len(word1)-1):
            merged_chars.append(word1[word1_curr_index:])
        
        if word2_curr_index <= (len(word2)-1):
            merged_chars.append(word2[word2_curr_index:])
        
        # merge the list into a single string
        result = "".join(merged_chars)

        return result

def main():
    solution = Solution()

    word1 = "abc"
    word2 = "pqr"
    print(solution.mergeAlternately(word1, word2)) # "apbqcr"

    word1 = "ab"
    word2 = "pqrs"
    print(solution.mergeAlternately(word1, word2)) # "apbqrs"

    word1 = "abcd"
    word2 = "pq"
    print(solution.mergeAlternately(word1, word2)) # "apbqcd"

if __name__ == "__main__":
    main()