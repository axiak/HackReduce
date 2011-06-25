#!/usr/bin/python
    
from collections import defaultdict
import sys
    

def main(argv):
  if len(argv) > 1:
    shift = int(argv[1])
  else:
    shift = 0

  line = sys.stdin.readline()

  book = None
  standard_scores, year_counts = defaultdict(int), defaultdict(int)
  book_variance, stock_variance = defaultdict(int), defaultdict(int)
  covariance_data = []
  covariances = {}

  last_key = None

  for line in sys.stdin:
    key, value, total, average = line.rstrip().split("\t")
    symbol, year, which = key.split("_") 

    if last_key != symbol and last_key is not None:
      v = covariance_data
      covariances[symbol] = sum(v[i][0] * v[i + shift][1] for i in range(max(0, shift), min(len(v), len(v) + shift)))
      covariance_data = []

    if which == 'book':
      book = dict(value=value, year=year, total=total, average=average, symbol=symbol)

    elif (which == 'symbol' and 
          book is not None and 
          book['total'] > 0 and 
          book['symbol'] == symbol and
          book['year'] == year):
      covariance_data.append(((float(book['value']) - float(book['average'])), (float(value) - float(average))))
      book_variance[symbol] += (float(book['value']) - float(book['average']))**2
      stock_variance[symbol] += (float(value) - float(average))**2
      year_counts[symbol] += 1

      book = None
    else:
      book = None

    last_key = symbol

  if last_key is not None:
    symbol = last_key
    v = covariance_data
    covariances[symbol] = sum(v[i][0] * v[i + shift][1] for i in range(max(0, shift), min(len(v), len(v) + shift)))
    covariance_data = []

  print covariances

  for symbol in year_counts:
    if year_counts[symbol] > 1:
      print symbol, ': ', covariances[symbol] / (stock_variance[symbol] * book_variance[symbol]) ** .5

if __name__ == "__main__":
  main(sys.argv)   
