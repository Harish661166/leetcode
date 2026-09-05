class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rQue = deque()
        dQue = deque()
        for i,v in enumerate(senate):
            if v == "R":
                rQue.append(i)
            else:
                dQue.append(i)
        while rQue and dQue:
            r = rQue.popleft()
            d = dQue.popleft()
            if r < d:
                rQue.append(r + n)
            else:
                dQue.append(d + n)
        if rQue:
            return "Radiant"
        else:
            return "Dire" 