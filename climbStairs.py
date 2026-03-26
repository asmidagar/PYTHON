#Leetcode 70
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def help(n):
            if n <= 2:
                return n
            if n in d:
                return d[n]
            temp =  help(n-1) +  help(n-2) 
            d[n] = temp
            return temp
            
        return help(n)    