import argparse


def add_func(a,b):
	return a - b

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--sub',mnargs=2, type=int, help='subtracts two numbers')
	args = parser.parse_args()

	if args.sub:
		print( add_func(args.sub[0], args.sub[1]))
	print(args)