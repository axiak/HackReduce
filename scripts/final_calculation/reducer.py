#!/usr/bin/python
    
import sys
    
def main(argv):
  line = sys.stdin.readline()

  # {symbol}_{year}_stock\t{ave_close_price}\t{sum_across_all_years}\t{average_across_all_years}
  # {symbol}_{year}_book\t{count}\t{total_count_across_all_years}\t{average_across_all_years}

  
  while line:
      print  "LongValueSum:" + word.lower() + "\t" + "1"
      line =  sys.stdin.readline()
  except "end of file":
    return None



if __name__ == "__main__":
main(sys.argv)   
