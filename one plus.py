
class Solution:
    def plusOne(self, num: List[int]) -> List[int]:
        result = int("".join(map(str,num)))
        result += 1

        return [int(num) for num in str(result)] 
    