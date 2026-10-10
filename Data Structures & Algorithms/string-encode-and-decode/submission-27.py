class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Special handling for list containing only an empty string
        if strs == [""]:
            return "~"
        
        # Otherwise, join the strings with "*" separator
        return "~".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        # Special handling for "*" which corresponds to a list with an empty string
        if s == "~":
            return [""]
        
        # Otherwise, split the string by "*" separator
        return s.split("~")
