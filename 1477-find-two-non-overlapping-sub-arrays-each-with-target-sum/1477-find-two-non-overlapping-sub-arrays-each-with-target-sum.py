class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        min_len = [INF] * n
        left = 0
        total = 0
        best = INF
        ans = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, length + min_len[left - 1])

                best = min(best, length)

            min_len[right] = best

        return -1 if ans == INF else ans