#! /usr/bin/env python3
from sys import argv
from genpb import genpb


def gennpb(targ_pattern, start_addr, curr_pattern=None, limit=1024):
	l = []
	addr = start_addr
	for i in range(len(targ_pattern)):
		cn = curr_pattern[i] if curr_pattern is not None else 0
		tn = targ_pattern[i]
		n = genpb(cn, tn, addr, 256, limit)
		print(f"{addr:02X} {cn:02X} {tn:02X}: {n}")
		l.append((addr, n))
		addr += 1
		addr %= 256
	return l


def main():
	with open(argv[1], 'rb') as file:
		targ_pattern = file.read()
	start_addr = int(argv[2], 16)
	curr_pattern = argv[3] if argv[3] != "Nulls" else None
	if curr_pattern is not None:
		with open(curr_pattern, 'rb') as file:
			curr_pattern = file.read()
	print(gennpb(targ_pattern, start_addr, curr_pattern))


if __name__ == '__main__':
	main()
