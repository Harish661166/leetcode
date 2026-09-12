class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lazy_trie = defaultdict(list)
        for word in words:
            lazy_trie[word[0]] += [word]
        
        res = 0
        for c in s:
            temp = list(lazy_trie[c])
            lazy_trie[c] = []
            while temp:
                word = temp.pop()
                if len(word) == 1:
                    res += 1
                else:
                    lazy_trie[word[1]] += [word[1:]]
        return res