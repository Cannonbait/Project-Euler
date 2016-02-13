import math

def first_ten():
	f = open('numbers', 'r')
	numbers = f.read().split('\n')
	num_sum = 0
	for num in numbers:
		num_sum += int(num)
	print(str(num_sum)[:10])

if __name__ == "__main__":
	first_ten()
