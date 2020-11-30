# Given a mathematical expression with just single digits,
# plus signs, negative signs, and brackets, evaluate the expression. 
# Assume the expression is properly formed.

# Example:
# Input: ( 3 + ( 2 - 1 ) ) + 5
# Output: 9

def doOp(a,b,op):
	if op == "+":
		return int(a) + int(b)
	elif op == "-":
		return int(a) - int(b)

def eval (expr):
	operators = []
	operands = []

	expr = "(" + expr + ")"

	for i in range(0,len(expr)):
		if expr[i] == " ": 
			continue

		elif expr[i].isdigit():
			operands.append(expr[i])
			continue

		elif expr[i] == "(":
			operators.append(expr[i])
			continue

		elif expr[i] == ")":
			while operators[-1] != "(" :
				b = operands.pop()
				a = operands.pop()
				op = operators.pop()
				operands.append(doOp(a,b,op))
			operators.pop()
			continue

		else: # it's an operator 
			operators.append(expr[i])
			continue

	result = operands.pop()
	if len(operators) == 1 and operators[0] == "-":
		result = result* -1
	return result
			



def main():
	expr = "( 3 + ( 2 - 1 ) ) + 5"
	print( "Expression: ", expr ,"=", eval(expr))

if __name__ == "__main__":
		main()