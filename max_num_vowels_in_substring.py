"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel_num = 0
        for i in range(len(s)-k+1):
            num_sub = len([sub for sub in s[i:i+k] if sub in ['a', 'e', 'i', 'o','u']])
            if num_sub > max_vowel_num:
                max_vowel_num = num_sub
        return max_vowel_num
    
if __name__ == "__main__":
    s, k = "aeiou", 2
    sol = Solution()
    print(sol.maxVowels(s,k))