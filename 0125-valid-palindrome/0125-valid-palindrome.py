class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        start=0
        end=len(s)-1
        while start<end:
            while start < end and s[start] not in a:
                start += 1
            while start < end and s[end] not in a:
                end -= 1
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True
            