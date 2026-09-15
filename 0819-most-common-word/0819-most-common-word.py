class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = ''.join([char if char.isalnum() or char.isspace() else ' ' for char in paragraph.lower()]).split()
        d = Counter(p)
        c = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        for i, e in c.items():
            if i not in banned:
                return i