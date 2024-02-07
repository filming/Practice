from typing import *

# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

''' Notes
- Multiplying the substring and comparing it with the bigger string takes O(m) in the worst case, as the multiplication operation for 
a string is linear to the size of the resulting string, and comparing two strings of length m takes O(m).
'''

''' Complexities 

Solution #1
Time Complexity: O(n * m)
Space Complexity: O(n)
'''

class Solution:
    # Solution 1
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # create a list that will store all of the GCD substrings we find, initializing it with a blank string in case we cannot find a GCD
        valid_gcd_substrs = [""]

        # determine which strings are the smallest/biggest (its not always garunteed that str2 is the smallest)
        if len(str1) < len(str2):
            smaller_string = str1
            bigger_string = str2
        else:
            smaller_string = str2
            bigger_string = str1

        # we need to make sure that the entire smaller string is in fact inside of the bigger string
        smallest_string_found = False
        left, right = 0, len(smaller_string)-1

        while right <= len(bigger_string):
            substr = bigger_string[left:right+1]

            if substr == smaller_string:
                smallest_string_found = True
                break

            left += 1
            right += 1
        
        # returning an empty string now if we know that the entire smaller string is not inside of the bigger string
        if smallest_string_found == False:
            return valid_gcd_substrs[-1]

        # now we need to find all the possible GCDs that exist for these two strings
        for i in range (1, len(smaller_string)+1):
            # checking to see if the length of the bigger string is divisible by the current value of i AND the same for the smaller string
            if ((len(bigger_string) % i) == 0) and ((len(smaller_string) % i) == 0):
                # create a substr of the first i chars of the smaller string
                smaller_string_substr = smaller_string[:i]

                # check and see if smallesr_string_substr when repeated to be of equal length of the bigger string, is an equivalent string
                if (smaller_string_substr * int((len(bigger_string) / i))) == bigger_string:
                    valid_gcd_substrs.append(smaller_string_substr)

        # returning the first element inside of our valid_gcd_substrs list
        return valid_gcd_substrs[-1]

def main():
    solution = Solution()

    str1 = "ABCABC"
    str2 = "ABC"
    print(solution.gcdOfStrings(str1, str2)) # "ABC"

    str1 = "ABABAB"
    str2 = "ABAB"
    print(solution.gcdOfStrings(str1, str2)) # "AB"

    str1 = "LEET"
    str2 = "CODE"
    print(solution.gcdOfStrings(str1, str2)) # ""

    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    print(solution.gcdOfStrings(str1, str2)) # "TAUXX"

    str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
    str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
    print(solution.gcdOfStrings(str1, str2)) # "NLZGM"

    str1 = "ABABABAB"
    str2 = "ABAB"
    print(solution.gcdOfStrings(str1, str2)) # "ABAB"

    str1 = "AAAAAAAAA"
    str2 = "AAACCC"
    print(solution.gcdOfStrings(str1, str2)) # "ABAB"

if __name__ == "__main__":
    main()
