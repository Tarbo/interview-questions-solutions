"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty."""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output_str = ""
        index = 0
        # index only to the minimum string length
        min_str_len = min([len(string) for string in strs])
        if min_str_len == 0:
            return output_str
        for index in range(min_str_len):
            curr_str = strs[0][index]
            for string in strs:
                if string[index] != curr_str:
                    return output_str
            output_str = output_str + curr_str
            index += 1
        return output_str

if __name__ == "__main__":
    strs = ["dog","racecar","car"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))