repo for hackreduce information.

format of n-gram data
---------------------

http://ngrams.googlelabs.com/datasets


format of stock data
---------------------



First Round
-----------
We are going to find correlations between frequency of company name mentions and their performance of the companies on the stock exchange.

Data Sets:
NYSE data (link)
Google Books Data


1.  Find yearly average stock prices
  Data set: NYSE
  Mapper Output: {symbol}_{year}\t{close_price}
  Reducer Output: {symbol}_{year}\t{ave_close_price}\t{count}

2.  Get yearly company mentions
  Data sets:  Google Book Data, Map of symbols 
  Mapper Output:  {company_name}_{year}\t{count}

3.  Translate company names to symbols
  Data set:  Mike's mapping from company name to symbol and the data set from above
  Output (no map reduce):  {symbol}_{year}\t{count}
  
4.  Find total stock price and average for all stocks and years (for use in correlation calculation)
  Data set:  Output from #1
  Mapper:  {symbol}_{year}\t{ave_close_price}\t{sum_across_all_years}\t{average_across_all_years}
  no reducer

    cat data_file_name.txt | python script_name.py > results.txt


Example of python script for a mapper can be found here:

http://docs.amazonwebservices.com/ElasticMapReduce/latest/GettingStartedGuide/
