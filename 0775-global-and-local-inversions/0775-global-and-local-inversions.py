class Solution:
    def isIdealPermutation(self, a: List[int]) -> bool:
        return all(i-2<v<i+2 for i,v in enumerate(a))