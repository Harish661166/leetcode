class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}   # prefix sum 0 has appeared once before we start

        curr = 0
        cnt = 0

        for num in nums:
            curr += num

            # Need a previous prefix sum such that:
            # curr - previous = k
            # previous = curr - k
            if curr - k in freq:
                cnt += freq[curr - k]

            # Record current prefix sum
            freq[curr] = freq.get(curr, 0) + 1

        return cnt


        
        
        
        

        