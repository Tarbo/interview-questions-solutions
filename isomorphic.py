"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character."""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s = len(set(s))
        len_t = len(set(t))
        if len_s != len_t:
            return False
        dict_s = {char:'ff' for char in set(s)}
        dict_t = {char: 'tt' for char in set(t)}
        for s_item, t_item in zip(s, t):
            if dict_s[s_item] == 'ff' and dict_t[t_item] == 'tt':
                dict_s[s_item] = t_item
                dict_t[t_item] = 1
            elif (dict_s[s_item] == 'ff' and dict_t[t_item] != 'tt') or (dict_s[s_item] != 'ff' and dict_t[t_item] == 'tt') or (dict_s[s_item] != t_item):
                return False
        return True
    
if __name__ == "__main__":
    s = "bbbaaaba"
    t = "aaabbbba"
    sol = Solution()
    print(sol.isIsomorphic(s,t))