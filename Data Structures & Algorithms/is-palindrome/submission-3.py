class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_data = ''.join(i.lower() for i in s if i.isalnum())
        
        return string_data == string_data [::-1]

        