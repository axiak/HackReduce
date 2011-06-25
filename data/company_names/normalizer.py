#!/usr/bin/python

import sys
import re

bad_re = re.compile(r'[/\\]\w{1,2}/?')
bad_re2 = re.compile(r'/?\w{1,2}/')

map = {}

for line in sys.stdin:
	symbol, name = line.lower().strip().split('\t', 1)
	tokens = bad_re2.sub('', bad_re.sub('', line.replace('&amp;', '&').replace('&#39;', "'").lower())).split()
	for bad_token in 'co inc corp /de /de/ /fi /fi/ /inc/de/ inc/de lp ltd ltd/cn group'.split():
		try:
			tokens.remove(bad_token)
		except:
			pass
		try:
			tokens.remove(bad_token + '.')
		except:
			pass
	map[symbol] = ' '.join(x for x in tokens if len(x) > 1).strip().strip(',')

print "    final static Map<String, String> COMPANY_NAMES = new HashMap<String, String>();"
print "    {"

for key, value in map.items():
    print '        COMPANY_NAMES.put("%s", "%s");' % (value, key)
print "    }"
