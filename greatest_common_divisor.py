"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
from typing import List


class Solution:
    @staticmethod
    def check_divisibility(s:List[str], prefix:List[str])->bool:
        return s == prefix * (len(s)//len(prefix))
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        list1, list2 = list(str1), list(str2)
        candidates = {}
        i = 0
        min_l = min(len(list1),len(list2))
        while i < min_l:
            i += 1
            prefix = list2[:i]
            print(f"{i}:\t{prefix}")
            if Solution.check_divisibility(list1, prefix) & Solution.check_divisibility(list2,prefix):
                l = len(prefix)
                candidates[l] = "".join(prefix)
        if candidates:
            return candidates[max(candidates.keys())]
        return ""

if __name__ == "__main__":
    solution = Solution()
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    print(solution.gcdOfStrings(str1, str2))