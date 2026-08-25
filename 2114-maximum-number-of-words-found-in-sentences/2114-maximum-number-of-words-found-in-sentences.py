class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer=0
        for i in range(len(sentences)):
            words=sentences[i].count(" ")+1
            if words>answer:
                answer=words
        return answer