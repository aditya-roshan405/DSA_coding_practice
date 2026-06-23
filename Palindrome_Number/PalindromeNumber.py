class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0                           # initially 

        while x > reversed_half:
            last_digit = x % 10                     # extract last digit from x
            reversed_half = reversed_half * 10 + last_digit 
            x = x // 10                             # remove last digit from x

        return x == reversed_half or x == reversed_half // 10