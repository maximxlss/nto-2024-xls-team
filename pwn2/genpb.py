#! /usr/bin/env python3
from sys import argv


def genpb(curr_value, targ_value, add_value, mod=256, limit=1024):
	val = curr_value
	c = 0
	if (curr_value == targ_value): return 0
	for i in range(limit):
		c += 1
		val += add_value
		val %= mod
		if val == targ_value:
			return c
	return -1


def main():
	curr_value = int(argv[1], 16)
	targ_value = int(argv[2], 16)
	add_value = int(argv[3], 16)
	mod = int(argv[4])
	limit = int(argv[5])
	print(genpb(curr_value, targ_value, add_value, mod, limit))


if __name__ == '__main__':
	main()
