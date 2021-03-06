#Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#determine if the input string is valid.
#Input: "()", Output: true
#Input: "()[]{}", Output: true
#Input: "(]", Output: false
#Input: "([)]", Output: false
class Solution:
    def validpar(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
