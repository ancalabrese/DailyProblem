# Given an array of integers where each element represents the max number of steps that can be made forward
# from that element. 
# Write a function to return the minimum number of jumps to reach the end of the array 
# (starting from the first element). If an element is 0, they cannot move through that element.
# Example:
# Input: [3, 2, 5, 1, 1, 9, 3, 4]    
#		 [0, n, n, n, n, n, n, n]
# Output: 2
# Explanation:

# The minimum number of jumps to get to the end of the list is 2:
# 3 -> 5 -> 4

# Solution provided: O(n^2)
	# create a min jumps array 
	# jumps[i] will be equal to the min jumps needed to reach array[i] from array[0]
	# Create an outer loop with index i from 1 to len(array)-1 -> this will traverse the array starting from array[1]
	# Create an inner loop with index j from 0 to i -> the inner loop will populate the jumps array
	# for each step at j -> can I reach i from array[j] ? -> if array[j] > i: 
	# If I can reach, check the current # of jumps and compare it with any existing one and pick the min ->
	# jumps[i] = min(jumps[i], jumps[j]+1) 
	# break the j loop and advance i 
	# when we're done the answer is in the last position in jumps

def jumpToEnd(nums):
	arrayLength = len(nums)-1
	jumps = [float('inf') for i in range(arrayLength)]

	if nums[0] == 0 or  arrayLength == 0:
		return float('inf')

	jumps[0] = 0

	for i in range(1, arrayLength):
		for j in range(i):
			if nums[j] >= i -j and jumps[j] != float('inf'):
				jumps[i] = min(jumps[j]+1,jumps[i])
				break

	return jumps[len(jumps)-1]





#Solution provided: Recursive O(n^n)
# At each step check if the array is length==1 (no more position available)
# And check if first element is 0 (from here we can't move anywhere)
# From range array[1] check all the reachable position (array[0])
# num of jumps = to the value reurned from recursion passing array[i:] to the function
# once checked all position if num of Jumps+1 (take in account last jump) < than min -> min = jumps+1

def jumpToEndRecursive(nums):
	length = len(nums) - 1

	if length == 1: 
		return 0;

	if nums[0] == 0:
		return float('inf')

	min = float('inf')

	for i in range(1, nums[0]):
		if i < length:
			jumps = jumpToEndRecursive(nums[i:])
			if jumps != float('inf') and jumps + 1 < min:
				min = jumps+1

	return min
  
print jumpToEndRecursive([3, 2, 5, 1, 1, 9, 3, 4])
print jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])
# 2
