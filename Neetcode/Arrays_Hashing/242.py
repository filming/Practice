from typing import *

# https://leetcode.com/problems/valid-anagram/

'''notes
'''

'''approach
Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def isAnagram(self, s: str, t: str) -> bool:
        char_occurrences = {}

        for curr_char in s:
            if curr_char in char_occurrences:
                char_occurrences[curr_char] += 1
            else:
                char_occurrences[curr_char] = 1
        
        for curr_char in t:
            if curr_char in char_occurrences:
                char_occurrences[curr_char] -= 1
            else:
                return False # t contains a letter that does not exist in s, cannot be an anagram
        
        for curr_occurrence in char_occurrences.values():
            if curr_occurrence != 0:
                return False # s and t contained a different amount of the same character, cannot be an anagram
            
        return True

def main():
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t)) # true

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t)) # false

if __name__ == "__main__":
    main()