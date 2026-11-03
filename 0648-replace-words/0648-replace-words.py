class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence=sentence.split()
        for i in range(len(sentence)):
            for j in range(len(dictionary)):
                if sentence[i].startswith(dictionary[j]):
                    if len(dictionary[j])<len(sentence[i]):
                        sentence[i]=dictionary[j]
        return " ".join(sentence)