#!/usr/bin/python

import sys

#Sample Data:
#symbol_year	closeprice
#GE_1985	15.00

def main():
    # maps words to their counts
	symbol_data = {}

	
	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
	
		# parse the input we got from mapper.py
		symbol_year, closeprice = line.split('\t', 1)
		try:
			closeprice = float(closeprice)
			#symbolcount[symbol] = symbolcount.get(symbol, 0) + count
		except ValueError:
			# price was not a number, so silently
			# ignore/discard this line
			continue
		avg, count = symbol_data.get(symbol_year, (0, 0))
		avg = (avg * count + closeprice) / (count + 1)
		count += 1
		symbol_data[symbol_year] = (avg, count)
	
	for key, value in symbol_data.iteritems():
		print '%s\t%s\t%s' % (key, value[0], value[1])
		
if __name__ == '__main__':
    main()