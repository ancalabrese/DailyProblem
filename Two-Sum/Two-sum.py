# Given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.
# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.

# def two_sum(list, k):
#   # Fill this in.

# print two_sum([4,7,1,-3,2], 5)
# # True

# Try to do it in a single pass of the list.

#Proposed Solution: O(n)
# For each number in the list get the complementary betewen target and number c= k-list[i]
# Add d to a second list of "required numbers"
# At each step check if list[i] is in required if not add n to required list otherwise return true


def printTwoSum(numbers, target):
	required = []
	for n in numbers:
		c = target - n
		for r in required:
			if r == c:
				print("Found pair", r, n)
				return True
			
		required.append(n) 
	return False

def main():
	numbers = [4,7,1,-3,2]
	k = int(input("Insert target number: "))
	print("List of numbers: ", numbers)
	print(printTwoSum(numbers, k))

    

if __name__ == "__main__":
    main()