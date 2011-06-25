#!/usr/bin/python
    
from collections import defaultdict
import sys
from itertools import chain
    
def main(argv):
  line = sys.stdin.readline()

  data = defaultdict(lambda: defaultdict(list))
  symbols = dict
  while line:
    key, score = line.rstrip().split("\t")
    symbol, year, which = key.split("_") 

    data[year][which].append(dict(symbol=symbol, score=float(score)))

    line = sys.stdin.readline()
    
  for i in (range(-5, 5)):
    for year in data:
      offset_year = str(int(year) + i)
      if data.has_key(offset_year):
        print "%s\t%f" % (i, correlation(data[year]['symbol'], data[offset_year]['book']))


def correlation(list1, list2):
  last_symbol, last_score, total, count = (None, 0, float(), 0)

  for item in sorted(chain(list1, list2), key=lambda item: item['symbol']):
    if last_symbol != item['symbol']:
      last_symbol = item['symbol']
      last_score = item['score']
    else:
      total += last_score * item['score']
      count += 1

      
  return total / count if count > 0 else 0


if __name__ == "__main__":
  main(sys.argv)   
