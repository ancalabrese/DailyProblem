# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
# subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Propsed solution: O(n)
# 1. Iterate through list
# 2. Sum all items from start to current item
# 3. If sum is < than s move to next item
# 	 Else compare sub array lenght with min_length -> if smaller:
		# 1. Update min_lenght
		# 2. Update current sum value removing start element  
		# 3. Update start postion to start + 1


class Solution:
  def minSubArrayLen(self, nums, s):
  	min_length = len(nums) + 2
  	start = 0
  	i = 0
  	sum = nums[i]
  	while i < len(nums):
  		if sum < s:
  			i +=1
  			if(i > len(nums) -1):
  				break
  			sum = sum + nums[i]
  			continue
  		else:
  			length = i - start + 1
  			if length < min_length:
  				min_length = length
  			sum = sum - nums[start]
  			start = start+1
  			continue
  	return length
    


print (Solution().minSubArrayLen([2,3,1,2,4,3], 7))
# 2