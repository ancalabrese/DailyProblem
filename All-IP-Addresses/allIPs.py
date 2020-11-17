# An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

# Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

# Keep in mind that integers can't start with a 0! (Except for 0)

# Example:
# Input: 1592551013
# Output: ['159.255.101.3', '159.255.10.13']
# def ip_addresses(s, ip_parts=[]):
#   # Fill this in.

# print ip_addresses('1592551013')
# # ['159.255.101.3', '159.255.10.13']

# Solution: O(n3) where n cannot be greater than 12
# The approach insert dots in the provided string and then tries all the combination checking if ip parts could be valid 


def isValid(ip):
	ip = ip.split(".")
	for i in ip:
		if len(i) > 3 or int(i) < 0 or int(i) > 255:
			return False
		if len(i) > 1 and int(i) == 0:
			return False
		if len(i) > 1 and i[0] == '0':
			return False
	return True


def ip_addresses(s):
	newIP = s
	size = len(s)
	res =[]

	if size > 12:
		return ["No valid ip found"]

	for i in range(1,size -2):
		for j in range (i+1, size-1):
			for k in range(j+1,size):
				newIP = newIP[:k]+"."+newIP[k:]
				newIP = newIP[:j]+"."+newIP[j:]
				newIP = newIP[:i]+"."+newIP[i:]

				if isValid(newIP):
					res.append(newIP)
				newIP = s
	return res


def main():
	print(ip_addresses('1592551013'))


if __name__ == "__main__":
    main()