from typing import *

# https://leetcode.com/problems/group-anagrams/

'''notes
- You can't store a unhashable obj as a key in a dict (such as a set or dict), so you must convert it into a hashable obj first (such as a tuple)
'''

'''approach
Solution #1
Time Complexity: O(n * klogk)
Space Complexity: O(n)

Solution #2
Time Complexity: O(N * KlogK)
Space Complexity: O(N * K)
'''

from typing import *

class Solution:
    # Solution 1
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = {}

        for curr_word in strs:
            curr_word_char_occurrences = {}

            # create a char occurrence dict of the current word in strs
            for curr_char in curr_word:
                if curr_char in curr_word_char_occurrences:
                    curr_word_char_occurrences[curr_char] += 1
                else:
                    curr_word_char_occurrences[curr_char] = 1
            
            # create a tuple of the current char occurrence (each occurrence sorted based on the char)
            curr_word_char_occurrences_tuple = tuple(sorted(curr_word_char_occurrences.items()))

            if curr_word_char_occurrences_tuple in anagram_groups:
                anagram_groups[curr_word_char_occurrences_tuple].append(curr_word)
            
            else:
                anagram_groups[curr_word_char_occurrences_tuple] = [curr_word]
        
        return anagram_groups.values()

    # Solution 2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for curr_word in strs:
            curr_word_sorted_tuple = tuple(sorted(curr_word))

            if curr_word_sorted_tuple in result:
                result[curr_word_sorted_tuple].append(curr_word)
            else:
                result[curr_word_sorted_tuple] = [curr_word]

        return result.values()

def main():
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]

    strs = [""]
    print(solution.groupAnagrams(strs)) # [[""]]

    strs = ["a"]
    print(solution.groupAnagrams(strs)) # [["a"]]

if __name__ == "__main__":
    main()