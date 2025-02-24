class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        result = ""
        first = s[0]
        last = s[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i] :
                return result

            result += first[i]

        return result