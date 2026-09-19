class Solution:
    def longestMountain(self, a: List[int]) -> int:
        return max((k+l+1 for (q,k),(p,l) in pairwise(
            (q,abs(sum(g))) for q,g in groupby((v<u)-(v>u) for v,u in pairwise(a))) 
                if q==1==-p),default=0)