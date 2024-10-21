class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums)== 2:
            return max(nums[0],nums[1])
        else:
            prev2=nums[0]
            prev=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            current=max(prev2+nums[i], prev)
            prev2=prev
            prev=current
        
        return current
        


        