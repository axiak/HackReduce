#!/usr/bin/python
import sys

def main():
	d = {}
	for line in sys.stdin:
		ticker, rest = line.strip().split('\t', 1)
		d[ticker.lower()] = rest

	f = open('/tmp/data')
	x = []
	for line in f:
		a, b = line.strip().split(' : ')
		x.append((d[a.lower()], b))

	x.sort(key = lambda a: abs(float(a[1])))
	for k, v in x:
		print "%s: %s" % (k, v)


if __name__ == "__main__":
	main()
