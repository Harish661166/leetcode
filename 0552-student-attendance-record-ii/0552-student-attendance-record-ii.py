class Solution:
    def checkRecord(self, n: int) -> int:
        # dp1 (a_i, a_{i-1}, a_{i-2}): answer, number of records of length i that are eligible for attendance award
        # If ends with P, a_{i-1}
        # If ends with A, b_{i-1}
        # If ends with PL, a_{i-2}
        # If ends with AL, b_{i-2}
        # If ends with PLL, a_{i-3}
        # If ends with ALL, b_{i-3}, NB: "LLL" is not eligible
        # dp2 (b_i, b_{i-1}, b_{i-2}): number of records of length i that do not have any absent "A", but are still eligible for attendance award
        # If ends with P, b_{i-1}
        # If ends with PL, b_{i-2}
        # If ends with PLL, b_{i-3}, NB: "A" is not allowed
        ai, ai1, ai2 = 3, 1, 0
        bi, bi1, bi2 = 2, 1, 1
        for i in range(1, n):
            ai, ai1, ai2 = (ai+bi+bi1+ai1+bi2+ai2) % int(1e9+7), ai, ai1
            bi, bi1, bi2 = (bi+bi1+bi2) % int(1e9+7), bi, bi1
        
        return ai