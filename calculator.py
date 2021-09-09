import argparse

def add_func(a,b):
	return a + b

def div_func(a, b):
	if b == 0:
		return f"ERROR: second number entered can not be 0"	
	return a / b

def remainder_func(a,b):
	if b != 0:
		return a % b
	return "The second number cant't be 0"

def sqrt(n):
    return n**2

def multiply_func(a,b):
    return a * b

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--add', nargs=2, type=int, help='adds two numbers')
	parser.add_argument('--divide', nargs=2, type=int, help='divides two numbers')
	parser.add_argument('--add',nargs=2, type=int, help='adds two numbers')
	parser.add_argument('--remainder',nargs=2, type=int, help='returns the remainder of two numbers')
	parser.add_argument('--sqrt', nargs =1, type=int, help='square roots a number')
	parser.add_argument('--multiply', nargs='+', type=int, help='multiply more then one numbers')
	args = parser.parse_args()

	if args.add:
		print( add_func(args.add[0], args.add[1]))

	if args.divide:
		print( div_func(args.divide[0], args.divide[1]))

	if args.remainder:
		print(remainder_func(args.remainder[0], args.remainder[1]))

	if args.multiply:
    		print(multiply_func(args.add[0],args[1]))		
	
	if args.sqrt:
		print( sqrt(args.sqrt[0]))

	if args.multiply:
    		print(multiply_func(args.add[0],args[1]))


