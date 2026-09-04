class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expect_sum = n*(n+1)//2
        act_sum = sum(nums)
        expect_squar_sum = n*(n+1)*(2*n+1)//6
        act_squar_sum = sum(i*i for i in nums)
        difrnc = act_sum - expect_sum  ## duplciate - missing
        sqr_diffrnc = act_squar_sum - expect_squar_sum ## duplciate ** 2 - missing**2
        dupl_plus_miss = sqr_diffrnc // difrnc
        duplicate = (difrnc + dupl_plus_miss)//2
        missing = duplicate - difrnc
        return [duplicate,missing]