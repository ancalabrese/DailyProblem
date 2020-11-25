# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0.
# Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]


class Solution(object):
  def threeSum(self, nums):
  	triplets = []
  	for i in range (len(nums)-2): 
  		res = set()
  		for j in range(i+1,len(nums)-1):
  			partial = -(nums[i] + nums[j])
  			if partial in res: 
  				t = [partial, nums[i], nums[j]]
  				triplets.append(t)
  			else:
  				res.add(nums[j])
  	return triplets

def main():
	nums = [1, -2, 1, 0, 5]
	print(Solution().threeSum(nums))
	# [[-2, 1, 1]]

if __name__ == "__main__":
	main()