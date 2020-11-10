# Hi, here's your problem today. This problem was recently asked by Apple:

# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.


# Proposed Solution: O(n)
# Traverse string a, and check wether shifting the string around we get b

def is_shifted(a, b):
	if(len(a) != len(b)):
		return False
	if(a == b):
		return True

	for i in range(1,len(a)):
	 new = a[i:]+ a[:i]
	 if new == b:
	 	return True

	return False


 
def main():
	print (is_shifted('abcde', 'cdeab'))
	print (is_shifted('abc', 'acb'))
    

if __name__ == "__main__":
    main()