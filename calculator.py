import argparse


def add_func(a,b):
	return a + b

sqrt_function
def sqrt(n):
    return n**2


def multiply_func(a,b):
    return a * b


if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--add',nargs=2, type=int, help='adds two numbers')

	parser.add_argument('--sqrt', nargs =1, type=int, help='square roots a number')

	parser.add_argument('--multiply', nargs='+', type=int, help='multiply more then one numbers')

	args = parser.parse_args()

	if args.add:
		print( add_func(args.add[0], args.add[1]))
	print(args)

	if args.sqrt:
		print( sqrt(args.sqrt[0]))


	if args.multiply:
    		print(multiply_func(args.add[0],args[1]))
	print(args)			

