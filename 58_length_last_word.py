class Solution:
    def lengthOfLastWord(self,s: str)->int:
        signs = ['"','.','!','¡','?',',','(',')','[',']','{','}','#','$']
        string_none_signs = ''.join([character for character in s if character not in signs])
        return len(string_none_signs.split()[-1])

test = Solution()
last_word = test.lengthOfLastWord('The last word is "moon" with length 4.')
print(last_word)
