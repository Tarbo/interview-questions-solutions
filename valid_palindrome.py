"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        pattern = r'[^a-z0-9]'
        cleaned_s = re.sub(pattern, "", s_lower)
        if len(cleaned_s) == 0 or len(cleaned_s) == 1:
            return True
        max_len = len(cleaned_s)
        max_check_length = max_len//2
        for i in range(max_check_length):
            if cleaned_s[i] != cleaned_s[max_len-i-1]:
                return False
        return True
    
if __name__ == "__main__":
    s = "race a car"
    sol = Solution()
    print(sol.isPalindrome(s))

