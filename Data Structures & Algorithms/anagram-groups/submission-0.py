class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item in new_dict.keys():
                new_dict[sorted_item].append(item)
            else:
                new_dict[sorted_item] = [item]
        return list(new_dict.values())
        