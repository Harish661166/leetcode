class Solution:
    def magicalString(self, n: int) -> int:
        vals= ['1', '2'] 
        s= '122'  
        cur= 0
        idx= 2

        while len(s)< n:
            for _ in range(int(s[idx])):
                s+= vals[cur]
                
            cur ^= 1
            idx += 1
        cnt= 0
        
        for x in range(n):
            if s[x] == '1':
                cnt+= 1
        
        return cnt
