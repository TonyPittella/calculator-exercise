import argparse


def add_func(a,b):
	return a + b

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--add',mnargs=2, type=int, help='adds two numbers')
	args = parser.parse_args()

	if args.add:
		print( add_func(args.add[0], args.add[1]))
	print(args)