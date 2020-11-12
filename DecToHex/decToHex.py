# Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string.
# Do not use any builtin base conversion functions like hex.
# Proposed Solution: O(n)
# Divide n by 16 and recursively repeat assign the result of division as n. 
# The reminder of each division is the least significant digit at the specific cycle
# A dictonary is used to map values from 10 to 15 to align letters as per base16 specifications

dexMap={10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F'}

def to_hex(n):
    R=0
    results=[]
    if n == 0:
	    return []
    else:
        R=n%16
        results.extend(to_hex(n/16))
        
    if R<10:
        results.append(R)
    else:
        results.append(dexMap[R])
    s = ''.join(str(e) for e in results) 
    return s

def main():
    print(to_hex(80))

if __name__ == '__main__':
    main()
