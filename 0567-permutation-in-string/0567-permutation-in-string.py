class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashmap1={}
        for ch in s1:
            hashmap1[ch]=hashmap1.get(ch,0)+1
        lenght_s1=len(s1)
        hashmap={}
        for i in range(lenght_s1):
            hashmap[s2[i]]=hashmap.get(s2[i],0)+1
        if hashmap==hashmap1:
            return True
        i=0
        j=lenght_s1
        while j < len(s2):
            if hashmap[s2[i]] == 1:
                hashmap.pop(s2[i])
            else:
                hashmap[s2[i]]-=1
            hashmap[s2[j]]=hashmap.get(s2[j],0)+1
            if hashmap==hashmap1:
                return True
            i+=1
            j+=1
        return False