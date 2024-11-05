
def subsetSumToK(n, k, arr):
    dp = [[0 for _ in range(k+1)] for _ in range(n)]
    # print("memo : " +helper(n-1,k,arr,dp))

    for i in range(0,n-1):
        dp[i][0]= True
    
    if arr[0] <= k:
        dp[0][arr[0]] = True

    for index in range(1,n):
        for target in range(1,k+1):  
            notTake = dp[index-1][target]
            take = False

            if notTake == False : 
                if arr[index] <= target:
                    take = dp[index-1][target-arr[index]]
            dp[index][target]= take or notTake
    print(dp)
    return dp[n-1][k]


from typing import List

def findWays(arr: List[int], k: int) -> int:
    n=len(arr)
     # Initialize a DP array where dp[i][target] will store the count of subsets up to index i that sum to target
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    zeros=0
    
    # Base case: There's one way to achieve target sum of 0 (by choosing no elements)
    for i in range(n):
        if arr[i] == 0:
            zeros+=1
        dp[i][0] = 1
    
    # Initialize first row (if arr[0] <= k, then we have one subset which includes only arr[0])
    if arr[0] <= k:
        dp[0][arr[0]] = 1
    
    # Fill the dp table
    for index in range(1, n):
        for target in range(k + 1):
            # Option 1: Do not include the current element arr[index]
            notTake = dp[index - 1][target]
            
            # Option 2: Include the current element arr[index], if it's not greater than the target
            take = 0
            if arr[index] <= target:
                take = dp[index - 1][target - arr[index]]
            
            # Sum both options
            dp[index][target] = notTake + take

    # The result is the count of subsets that sum to k using all elements
    return dp[n - 1][k]



# memoiation approach
# def helper(index,target,arr,dp):

#     if target == 0:
#         return True

#     if index == 0 :
#         return ( arr[0] == target )

#     if dp[index][target] != -1:
#         return dp[index][target]
#     notTake = helper(index-1, target, arr,dp)
#     take = False

#     if notTake == False : 
#         if arr[index] <= target:
#             take = helper(index-1,target-arr[index],arr,dp)

#     dp[index][target]= take or notTake

#     return dp[index][target]

def driver():
    # Fixed input
    n = 3
    arr = [12 ,14 ,3, 18, 2] 
    k = 13

    # Call the subsetSumToK function
    result = subsetSumToK(n, k, arr)
    count = findWays(arr,k)

    print(count)

    # Print the result
    if result:
        print(f"There exists a subset in {arr} that sums to {k} {count} times.")
    else:
        print(f"No subset in {arr} sums to {k}.")

# Run the driver function
driver()
