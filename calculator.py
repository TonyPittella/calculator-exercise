import argparse


def add_func(a,b):
	return a + b

def multiply_func(a,b):
    return a * b

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	#add arguments here
	parser.add_argument('--add',nargs=2, type=int, help='adds two numbers')
	parser.add_argument('--multiply', nargs=2, type=int, help='multiply two numbers')
	args = parser.parse_args()

	if args.add:
		print( add_func(args.add[0], args.add[1]))
	print(args)


	if args.multiply:
    		print(multiply_func(args.add[0],args[1]))
	print(args)			
	