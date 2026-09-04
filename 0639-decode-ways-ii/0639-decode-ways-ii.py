class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def decode(i: int) -> int:
            if i < 0: return 1
            decodings = 0
            if s[i] == "*":
                decodings = 9 * decode(i - 1) % MOD
                if i == 0: return decodings
                prev_char = s[i - 1]
                if prev_char == "1": decodings = (decodings + 9 * decode(i - 2)) % MOD
                if prev_char == "2": decodings = (decodings + 6 * decode(i - 2)) % MOD
                if prev_char == "*": decodings = (decodings + 15 * decode(i - 2)) % MOD
            else:
                if s[i] != "0": decodings = decode(i - 1) % MOD
                if i == 0: return decodings
                prev_char = s[i - 1] 
                if prev_char == "1": decodings = (decodings + decode(i - 2)) % MOD
                if prev_char == "2" and s[i] <= "6": decodings = (decodings + decode(i - 2)) % MOD
                if prev_char == "*":
                    decodings = decodings = (decodings + decode(i - 2)) % MOD
                    if s[i] <= "6": decodings = (decodings + decode(i - 2)) % MOD
            return decodings

        return decode(len(s) - 1)