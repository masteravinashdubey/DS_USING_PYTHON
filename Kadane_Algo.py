# Given an integer array arr[]. You need to find and return the maximum sum possible from all the subarrays (subarray is required to be contiguous).
# E.g. : arr=[1,2,3,-2,5] subarrays={[1][2][3][-2][5][1,2][2,3][3.-2][-2,5][1,2,3][2,3,-2][3,-2,5][1,2,3,-2][2,3,-2,5][1,2,3,-2,5]} Total subarrays = n*(n+1)/2
# Sum all the subarray return maximum.

##Solution
#

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        n=len(arr)
        maxsum=arr[0]
        sum=arr[0]
        for i in range(1,n):
            sum = max(arr[i],sum+arr[i])
            maxsum=max(maxsum,sum)
            print(sum,maxsum)
        
        return maxsum

import math 

arr=[[1,2,3,-2,5],[-1,-2,-3,-4],[5,4,7],[-79, -68, -18, -58,25, 52, -68, -30, 6, 10]]
ob=Solution()
for i in range(len(arr)):
    print(ob.maxSubArraySum(arr[i]))