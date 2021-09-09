import argparse


def add_func(a,b):
	return a + b

def remainder_func(a,b):
	return a % b

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--add',nargs=2, type=int, help='adds two numbers')
	parser.add_argument('--remainder',nargs=2, type=int, help='returns the remainder of two numbers')
	args = parser.parse_args()

	if args.add:
		print( add_func(args.add[0], args.add[1]))
	print(args)

	if args.remainder:
		print(remainder_func(args.remainder[0], args.remainder[1]))
