# A majority element is an element that appears more than half the time.
# Given a list with a majority element, find the majority element.

# Here's an example and some starting code.

# Proposed Solution: O(n)
# Create an hashmap with key = the number and value = incremental counter. 
# Whenever we insert a new element and the counter is > than the number of elements in the array then return the current element


def main():
	print(majority_element([3, 5, 3, 3, 2, 4, 3]))		
	# 3


def majority_element(nums):
	distribution = {}
	for n in nums :
		if n not in distribution:
			distribution[n]=1
		else:
			distribution[n] = distribution[n]+1
		if distribution[n] > len(nums)/2:
			return n

	return "No majority element found"




if __name__ == "__main__":
    main()