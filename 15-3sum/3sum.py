class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        arr = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, len(nums)-1

            while l < r:
                curr_sum = nums[i]+nums[l]+nums[r]
                if  curr_sum == 0:
                    arr.append((nums[i],nums[l],nums[r]))
                    l += 1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1 
                elif curr_sum > 0:
                    r-=1
                elif curr_sum < 0:
                    l+=1
                
        return arr
        