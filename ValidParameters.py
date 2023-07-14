class Solution:
    def __init__(self):
        self.stack=[]
        self.mapping = {')': '(', '}': '{', ']': '['}
    def isValid(self, s: str) -> bool:
        for char in s:
            if char in self.mapping.values():  # Opening bracket
                self.stack.append(char)
            elif char in self.mapping.keys():  # Closing bracket
                if not self.stack or self.mapping[char] != self.stack.pop():
                    return False
        return len(self.stack) == 0
s = Solution()

# # Example usage:
# s = "(({}))"
# print(is_valid(s))  # Output: True

# s = "([)]"
# print(is_valid(s))  # Output: False

# s = "[({(())}[()])]"
# print(is_valid(s),8,"true")

# s = "[])"
# print(is_valid(s),6,"false")

# s = "[({])}"
# print(is_valid(s),7,"false")

# s = ")(){}"
# print(is_valid(s),5,"false")

