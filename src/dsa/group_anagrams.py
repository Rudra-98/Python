from ast import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1
            result.setdefault(tuple(count), []).append(str)

        return list(result.values())


strs = ["act","pots","tops","cat","stop","hat"]
o = Solution()
print(o.groupAnagrams(strs))


