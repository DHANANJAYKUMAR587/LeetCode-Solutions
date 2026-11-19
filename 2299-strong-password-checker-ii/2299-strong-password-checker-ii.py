class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        special="!@#$%^&*()-+"
        lower="abcdefghijklmnopqrstuvwxyz"
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digit="0123456789"
        ad=True
        for i in range(len(password)-1):
            if password[i]==password[i+1]:
                ad=False 
        lc=0
        uc=0
        sc=0
        dc=0            
        for i in password:
            if i in lower:
                lc+=1
            elif i in upper:
                uc+=1
            elif i in digit:
                dc+=1
            elif i in special:
                sc+=1
        if len(password)>=8:
            if lc>0 and uc>0 and sc>0 and dc>0:
                return ad
        return False