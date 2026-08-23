class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        
        threshold = len(nums)//3
        return [num for num,count in count.items() if count > threshold]
        