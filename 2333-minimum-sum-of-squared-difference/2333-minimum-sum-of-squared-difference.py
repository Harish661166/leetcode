class Solution:
    def minSumSquareDiff(self, a1: List[int], a2: List[int], k1: int, k2: int) -> int:
        k,a = k1+k2,[*map(abs,map(sub,a1,a2))]
        cost = lambda h:sum(max(0,v-h) for v in a)
        h = bisect_left(range(max(a)+1),1,key=lambda h:cost(h)<=k)
        return h and sum(min(v,h)**2 for v in a)-(k-cost(h))*(2*h-1)