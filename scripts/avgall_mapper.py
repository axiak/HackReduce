#!/usr/bin/python
import sys

#Input look like 
#MSFT_2001 54 10
#GOOG_2000 89 45
 
#Output look like 
#MSFT_2001 54 55 55/<count>
#MSFT_2002 1  55 55/2
#GOOG_2000 89 98 98/2
#GOOG_2010 9  98 98/2


def main():
    # maps words to their counts
	symbol_data  = {}

	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()
	
		# parse the input we got from mapper.py
		symbol_year, closeprice, cnt = line.split('\t', 2)
		try:
			closeprice = float(closeprice)
		except ValueError:
			# price was not a number, so silently
			# ignore/discard this line
			continue
		sum_price, avg, count = symbol_data.get(symbol_year, (0,0,0))
		avg = (avg * count + closeprice) / (count + 1)
		sum_price = sum_price + closeprice 
		count += 1
		symbol_data[symbol_year] = (sum_price, avg, count)
	
	for key, value in symbol_data.iteritems():
		print '%s\t%s\t%s\t%s' % (key, closeprice, value[0], value[1])
		
if __name__ == '__main__':
    main()
