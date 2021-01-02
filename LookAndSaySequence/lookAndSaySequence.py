# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:

# Each consecutive value describes the prior value.

# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

# Your task is, return the nth term of this sequence.


def nextSequenceValue(element):
	chars = str(element)
	prev = ''
	consecutive = 0
	value = ''
	for c in chars:
		if c == prev:
			consecutive+=1
		else: 
			if consecutive > 0:
				value += str(consecutive) + prev
			prev = c
			consecutive = 1
	value += str(consecutive) + prev
	return int(value)



sequence = [1,11]
for i in range(1,5):
	sequence.append(nextSequenceValue(sequence[i]))

print sequence 
