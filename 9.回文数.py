# python
# 281015 20220113
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif 0 <= x <= 9:
            return True
        else:
            x = str(x)
            if x[::1] == x[::-1]:
                return True
            else:
                return False
