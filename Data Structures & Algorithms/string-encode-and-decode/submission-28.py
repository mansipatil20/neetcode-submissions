class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i=0
        for _ in range(len(s)):
            if i >= len(s):
                break
            j = s.find("#",i)
            length = int(s[i:j])

            word = s[j+1 : j+1+length]
            decoded_str.append(word)
            i = j + 1 + length
                

        return decoded_str
