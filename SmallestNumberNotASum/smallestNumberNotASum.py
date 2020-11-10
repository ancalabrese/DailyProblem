# Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.

# Example:
# Input: [1, 2, 3, 8, 9, 10]
# Output: 7
# Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.

# Proposed solution: O(n)
# Lets set resolution to 1 -> the smallest amount possible
# For every element of the list if res is greater or equal than the element than res will be set to res + element
# Res always is always the smallest summable number in the sub-list + 1 (out of summable range). 
# If res is < than element then we found the solution. Being the list ordered the next sum will be greater in any case

def findSmallest(nums):
	res = 1 
	for i in range(0,len(nums)):
		if res >= nums[i]:
			res = res + nums[i]

		else:
			return res


print (findSmallest([1, 2, 3, 8, 9, 10]))
# 7
