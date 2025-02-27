# Question - to remove the elements from the list
class Solution:
    def removeElement(self, num: List[int], val: int) -> int:
        j = 0
        for x in num :
            if x != val :
                num[j] = x
                j += 1
        return j
    
