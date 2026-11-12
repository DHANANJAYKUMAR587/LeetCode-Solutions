class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alpha="abcdefghijklmnopqrstuvwxyz"
        ans=[]
        for i in key:
            if i not in ans and i in alpha:
                ans.append(i)
        d={}
        for i,j in zip(ans,alpha):
            d[i]=j
        result=[]
        for i in message:
            if i in d:
                result.append(d[i])
            else:
                result.append(i)
        return "".join(result)