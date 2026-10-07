class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sentence=sentence.split()
        for i in range(len(sentence)-1):
            if sentence[i][-1]!=sentence[i+1][0]:
                return False
        if sentence[-1][-1]!=sentence[0][0]:
            return False
        return True