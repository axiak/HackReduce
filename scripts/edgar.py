# Get company name for stock ticker

import urllib
import re
import sys

company_name_re = re.compile(r'class="companyName">([^<]+)')

def get_company_name(symbol):
    url = 'http://www.sec.gov/cgi-bin/browse-edgar?company=&match=&CIK=%s&filenum=&State=&Country=&SIC=&owner=exclude&Find=Find+Companies&action=getcompany' % symbol
    content = urllib.urlopen(url).read()
    m = company_name_re.search(content)
    if m:
        return m.group(1).trim()
    else:
        return None

def main():
    for line in sys.stdin():
        ticker = line.strip().split()[0]
        if ticker:
            print "%s\t%s" % (ticker, get_company_name(ticker))


if __name__ == '__main__':
    main()
