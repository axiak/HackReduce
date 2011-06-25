$
#Get the ticker_year and closingprice
import sys
#Sample Data:
#exchange,stock_symbol,date,stock_price_open,stock_price_high,stock_price_low,stock_price_close,stock_volume,stock_price_adj_close
#NYSE,GRT,1996-04-29,16.87,17.00,16.87,17.00,17500,3.75
#NYSE,GCH,1998-02-02,10.59,10.76,10.08,10.19,190000,4.73
################
#Data needed:
#Ticker: [1]  e.g.:GRT
#Date: [2]    e.g. :1996-04-29
#Closeprice:[6] e.g.: 17.00

def main():
    for line in sys.stdin:
        # remove leading and trailing whitespace
    	line = line.strip()
    	words = line.split()
    	#Get ticker, date and closing price
    	if words[0] != 'exchange'
			ticker=words[1].lower()
			date= words[2].split('-')
			year=date[0]
			closeprice=words[6]
			symbol_year=ticker+'_'+year
			print '%s\t%s' % (symbol_year,closeprice)

if __name__ == '__main__':
    main()