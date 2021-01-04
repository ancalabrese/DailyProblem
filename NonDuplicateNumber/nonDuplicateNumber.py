# Given a list of numbers, where every number shows up twice except for one number,find that one number.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1


def singleNumber(nums):
	values = {}
	for n in nums: 
		if n in values:
			values[n] +=1
		else:
			values[n] = 1
	for k in values:
		if values[k] == 1:
			return values[k]
	return None
	

def allSingleNumbers(nums):
	values = {}
	for n in nums: 
		if n in values:
			values[n] +=1
		else:
			values[n] = 1
	for k in list(values):
		if values[k] > 1:
			values.pop(k)
	return values.keys()

print singleNumber([4, 3, 2, 4, 1, 3, 2])
print allSingleNumbers([4, 3, 2, 3, 5, 7, 3, 5, 9, 8, 4, 1, 3, 2])
