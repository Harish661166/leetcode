import math
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """
        start=a, length=k(no of consecutive numbers we take )
        sum=k/2*(first+last), last term a+k-1
        sum=k(2a+k-1)/2 =n 
        ==> 2n=k(2a+k-1)
        ==> a=(2n/k-k+1)/2

        so instead of guessing start we guess length

        possible lengths, min sum of k numbers <=n ==> k(k+1)/2<=n 
        ==> k<=sqrt(2n)
        """
        ans=0
        # k (length) can only go up to √(2n) because even the smallest length-k sequence is 1+2+...+k.
        for k in range(2,int(math.sqrt(2*n))+1):
            if (2*n)%k==0: # if 2n/k is not an integer , then a cant be an integer
                x=(2*n)//k - k +1 # instead of 2a=2n/k-k+1
                # here 2a=x
                if x>0 and x%2==0: 
                    ans+=1
        return ans+1 