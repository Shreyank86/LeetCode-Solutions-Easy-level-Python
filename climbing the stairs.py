class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        third=0
        for i in range(n) :
            third = first + second
            first = second
            second = third

        result = third

        return result