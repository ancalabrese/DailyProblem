# Given a non negative number n convert it to binary without using any build in functions
# Proposed Solution: O(n)
# The reminder of n/2 is our least significant bit. Proceed recursively passing the result of n/2 until we get to 0 

def to_bin(n):
    res = []
    r = 0
    
    if n == 0 :
        return [0]
    
    r = n%2
    res.append(r)
    res.extend(to_bin(n/2))
    s = ''.join( str(e) for e in res)
    return s
    
    
    

def main():
    print(to_bin(2))

if __name__ == '__main__':
    main()
