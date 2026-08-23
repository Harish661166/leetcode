class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        p = 1  # position (units, tens, hundreds...)
        while p <= n:
            higher = n // (p * 10)
            current = (n // p) % 10
            lower = n % p

            if current == 0:
                count += higher * p
            elif current == 1:
                count += higher * p + lower + 1
            else:
                count += (higher + 1) * p

            p *= 10
        return count