"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        start_index, end_index = 0, len(s)-1
        s = list(s)
        while start_index < end_index:
            if s[start_index] in vowels and s[end_index] in vowels:
                s[start_index], s[end_index] = s[end_index], s[start_index]
                start_index += 1
                end_index -= 1
            if s[start_index] not in vowels:
                start_index += 1
            if s[end_index] not in vowels:
                end_index -= 1
        return ''.join(s)
    

if __name__ == "__main__":
    solution = Solution()
    s = "IceCreAm"
    print(solution.reverseVowels(s))  # AceCreIm

    s = "leetcode"
    print(solution.reverseVowels(s))  # leotcede

    s = "TarboMbeki"
    print(solution.reverseVowels(s))  # Aa

    s = "Adannaya"
    print(solution.reverseVowels(s))  # uUoOiIeEaA