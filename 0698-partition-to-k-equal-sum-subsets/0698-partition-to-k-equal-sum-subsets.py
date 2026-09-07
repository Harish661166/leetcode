class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        if nums[0] > total:
            return False

        s = total // k
        n = len(nums)

        def backtrack(total, visit, count, start):
            if count == k:
                return True
            for i in range(start, n):
                if i in visit:
                    continue
                if total + nums[i] > s:
                    continue
                # duplicate-pruning optimization
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visit:
                    continue
                visit.add(i)
                if total + nums[i] == s:
                    if backtrack(0, visit, count + 1, 0): return True
                else:
                    if backtrack(total + nums[i], visit, count, i + 1): return True
                visit.remove(i)
                if total == 0:
                    return False
            return False

        return backtrack(0, set(), 0, 0)