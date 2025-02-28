class Solution:
    def searchInsert(self, num: List[int], target: int) -> int:
        l = 0
        r = len(num) - 1

        while l<=r :
            mid = (l + r)//2

            if num[mid] > target :
                r = mid - 1 

            elif num[mid] < target :
                l = mid+1

            else :
                return mid

        return l