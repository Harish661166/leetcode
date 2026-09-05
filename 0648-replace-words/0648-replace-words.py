class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr = sentence.split()
        s = set(dictionary)

        def helper(word, s):
            for i in range(len(word)):
                root = word[0:i]

                if root in s:
                    return root

            return word

        for word in range(len(arr)):
            arr[word] = helper(arr[word], s)

        return ' '.join(arr)