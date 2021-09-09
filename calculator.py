import argparse


def add_func(a,b):
	return a + b

def div_func(a, b):
	return a / b

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--add', nargs=2, type=int, help='adds two numbers')
	parser.add_argument('--divide', nargs=2, type=int, help='divides two numbers')
	args = parser.parse_args()

	if args.add:
		print( add_func(args.add[0], args.add[1]))
	print(args)

	if args.divide:
		print( div_func(args.divide[0], args.divide[1]))