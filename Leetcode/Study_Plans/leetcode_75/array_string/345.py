from typing import *

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

'''notes
'''

'''approach
Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def reverseVowels(self, s: str) -> str:
        result, vowels = [], []

        # all vowels get placed as a _ in the result string for now, they'll be replaced in the next step
        valid_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for curr_char in s:
            if curr_char in valid_vowels:
                vowels.append(curr_char)
                result.append('_')
            else:
                result.append(curr_char)
        
        # iterate through result and replace each _ with the last vowel in the vowels list
        for i in range (len(result)):
            if result[i] == '_':
                result[i] = vowels.pop()

        return "".join(result)

def main():
    solution = Solution()

    s = "hello"
    print(solution.reverseVowels(s)) # "holle"

    s = "leetcode"
    print(solution.reverseVowels(s)) # "leotcede"

if __name__ == "__main__":
    main()