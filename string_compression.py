"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        previous_char = ''
        compressed_string = ''
        repeatation_count = 0
        if len(chars) == 1:
            return 1
        for i in range(len(chars)):
            if i == 0:
                previous_char = chars[i]
                repeatation_count += 1
            elif i == len(chars)-1:
                if chars[i] != previous_char:
                    compressed_string += previous_char
                    if repeatation_count != 1:
                        compressed_string += str(repeatation_count)
                    compressed_string += chars[i]
                else:
                    repeatation_count += 1
                    compressed_string += (previous_char + str(repeatation_count))
            else:
                if chars[i] != previous_char:
                    compressed_string += previous_char
                    if repeatation_count != 1:
                        compressed_string += str(repeatation_count)
                    previous_char = chars[i]
                    repeatation_count = 1
                else:
                    repeatation_count += 1
        chars[:] = list(compressed_string)
        return len(chars)
            
if __name__ == "__main__":
    sol = Solution()  
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(sol.compress(chars=chars))                
                

