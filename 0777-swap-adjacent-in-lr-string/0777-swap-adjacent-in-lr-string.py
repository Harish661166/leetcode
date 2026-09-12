class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
        i, j = 0, 0

        n = len(start)

        while i < n or j < n:

            while i < n and start[i] == 'X': i+=1
            while j < n and result[j] == 'X': j+=1

            if (i == n or j ==n ) and (i!=n or j!=n):
                return False

            if i == n and j == n:
                return True

            if start[i] != result[j]:
                return False

            if start[i] == 'R':
                if i > j:
                    return False
            
            if start[i] == 'L':
                if i < j:
                    return False
                
            i+=1
            j+=1
            
        
        return True