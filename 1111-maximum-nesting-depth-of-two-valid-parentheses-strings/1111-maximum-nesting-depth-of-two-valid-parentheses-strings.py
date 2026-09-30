class Solution:
    def maxDepthAfterSplit(self, seq):
        n = len(seq)
        r = [0] * n
        depth = 0
        for i in range(n):
            if seq[i] == '(':
                # Level of '(' is after opening
                depth += 1
                r[i] = depth & 1
                continue
            # Level of ')' is before closing
            r[i] = depth & 1
            depth -= 1
        return r