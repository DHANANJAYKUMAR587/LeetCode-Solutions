class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans=[]
        ans1=[]
        for idx,val in enumerate(s):
            if val=="a":
                ans.append(idx)
            else:
                ans1.append(idx)
        if len(ans)==0 or len(ans1)==0 or max(ans)<min(ans1):
            return True
        return False