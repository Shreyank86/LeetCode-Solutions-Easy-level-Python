class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_text = " ".join(s.split())
        st = cleaned_text.split(" ")
        last = st[-1]
        length = len(last)

        return length
    
