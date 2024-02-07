from typing import *

# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

''' Notes

'''

''' Complexities 

Solution #1
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def reverseWords(self, s: str) -> str:
        # create a list that will store all the list of words that we come across
        words = []

        # set up a flag that will let us know if we're dealing with leading/trailing or just whitespace in general
        # also set up a temp string that will store the chars of each word we come across
        is_whitespace = True
        curr_word = ""

        for curr_char in s:
            # if we've found a char that isn't a space, we can assume this is part of the curr_word
            if curr_char != ' ':
                is_whitespace = False
                curr_word += curr_char

            # if we found a whitespace but it's directly after a char that isn't one, we can assume this is the end of a word
            if curr_char == ' ' and (not is_whitespace):
                words.append(curr_word)
                curr_word = ""
                is_whitespace = True

        # add the remaining chars in the temp string to our list of words
        if len(curr_word) > 0:
            words.append(curr_word)

        # swap the positions of each word in our list of words
        left, right = 0, len(words)-1

        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
        
            left += 1
            right -= 1

        # use the join function to convert our list of words into a string
        return " ".join(words)

def main():
    solution = Solution()

    s = "the sky is blue"
    print(solution.reverseWords(s)) # "blue is sky the"

    s = "  hello world  "
    print(solution.reverseWords(s)) # "world hello"

    s = "a good   example"
    print(solution.reverseWords(s)) # "example good a"



if __name__ == "__main__":
    main()