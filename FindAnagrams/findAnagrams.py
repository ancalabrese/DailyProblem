# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

# Example:

# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

#Proposed Solution: O(n) 
#Convert each string to it's ascii value. Words with the same ASCII value are Anagrams

def groupAnagramWords(stringList):
	anagrams={}
	for s in stringList:
		sum = 0
		for c in s:
			sum+=ord(c)
		if sum not in anagrams:
			anagrams[sum] = [s]
		else:
			anagrams[sum].append(s)
	return anagrams

def main():
	print (groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]

    

if __name__ == "__main__":
    main()