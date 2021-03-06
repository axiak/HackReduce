#!/usr/bin/python
    
from collections import defaultdict
import sys
    
def main(argv):
  line = sys.stdin.readline()

  book = None
  standard_scores, year_counts = defaultdict(int), defaultdict(int)
  book_variance, stock_variance = defaultdict(int), defaultdict(int)
  covariance = defaultdict(int)

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
      covariance[symbol] += (float(book['value']) - float(book['average'])) * (float(value) - float(average))
      book_variance[symbol] += (float(book['value']) - float(book['average']))**2
      stock_variance[symbol] += (float(value) - float(average))**2
      year_counts[symbol] += 1

      book = None
    else:
      book = None

    line =  sys.stdin.readline()


  for symbol in year_counts:
    if year_counts[symbol] > 1:
      print symbol, ': ', covariance[symbol] / (stock_variance[symbol] * book_variance[symbol]) ** .5

if __name__ == "__main__":
  main(sys.argv)   
