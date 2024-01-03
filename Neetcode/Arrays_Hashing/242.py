from typing import *

# https://leetcode.com/problems/valid-anagram/

'''notes
'''

'''approach
Solution #1
Time Complexity: O(n)
Space Complexity: O(n)

Solution #2
Time Complexity: O(n)
Space Complexity: O(1)
- Use a fixed size list of 26, each index representing a letter. (0 is a, 1 is b, etc). This will help make the space constant no matter how big n is.
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
    
    # Solution 2
    def isAnagram(self, s: str, t: str) -> bool:
        char_occurrences = [0] * 26

        for curr_char in s:
            char_occurrences[ord(curr_char) - 97] += 1 # convert char to ascii number, then subtract 97 in order to find its corresponding index in char_occurrences list
        
        for curr_char in t:
            char_occurrences[ord(curr_char) - 97] -= 1
        
        for curr_occurrence in char_occurrences:
            if curr_occurrence != 0:
                return False # if a value isn't 0, that means there is a char mismatch between s and t, cannot be an anagram
        
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