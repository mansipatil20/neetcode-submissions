class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_str={}
        for s in strs:
            char_s = "".join(sorted(s))
            if char_s not in output_str:
                output_str[char_s] = []
            output_str[char_s].append(s)
            
        return list(output_str.values())
        