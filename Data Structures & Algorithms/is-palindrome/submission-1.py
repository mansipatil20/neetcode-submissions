class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_data = ''.join(i.lower() for i in s if i.isalnum())
        reverse_string= string_data [::-1]
        print(string_data)
        print(reverse_string)

        if string_data==reverse_string:
            return True
        else:
            return False
        