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

      stock_variance = (float(value) - float(average)) / float(total)
      book_variance = (float(book['value']) - float(book['average'])) / float(book['total'])

      print "%s_%s_symbol\t%s" % (symbol, year, stock_variance)
      print "%s_%s_book\t%s" % (symbol, year, book_variance)

      book = None
    else:
      book = None

    line =  sys.stdin.readline()



if __name__ == "__main__":
  main(sys.argv)   
