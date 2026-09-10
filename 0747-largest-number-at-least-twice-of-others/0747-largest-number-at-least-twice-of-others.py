class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ind=0
        max_ele=0

        for i in range(len(nums)):

            if(max_ele<nums[i]):
                max_ele=nums[i]
                max_ind=i
        
        for i in range(len(nums)):

            if(i!=max_ind):
                if(not nums[i]*2<=max_ele):
                    return -1
            
        return max_ind