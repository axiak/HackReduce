#!/usr/bin/python
    
from collections import defaultdict
import sys
    
def main(argv):
  line = sys.stdin.readline()

  book = None
  standard_scores, year_counts = defaultdict(int), defaultdict(int)
  while line:
    key, value, total, average = line.rstrip().split("\t")
    symbol, year, which = key.split("_") 

    if which == 'book':
      book = dict(value=value, year=year, total=total, average=average, symbol=symbol)

    elif (which == 'symbol' and 
          book is not None and 
          book['total'] > 0 and 
          book['symbol'] == symbol and
          book['year'] == year):

      stock_variance = (value - average) / total
      book_variance = (book['value'] - book['average']) / book['total']

      standard_scores[symbol] += stock_variance * book_variance
      year_counts[symbol] += 1

      book = None
    else:
      book = None

    line =  sys.stdin.readline()


  for symbol in standard_scores:
    print symbol, ': ', str(standard_scores[symbol] / (year_counts[symbol] - 1))


if __name__ == "__main__":
  main(sys.argv)   
