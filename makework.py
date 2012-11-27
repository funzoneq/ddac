#!/usr/bin/env python

from tasks import available

results = {}
lines = [line.strip() for line in open('tld.txt')]
for tld in lines:
	results[tld] = available.delay("arnoudvermeer", tld)

length = len(results.keys())

while length > 0:
	for k in results.keys():
		result = results[k]
		if result.ready():
			print length, k
			try:
				print result.get(timeout=1)
			except:
				pass
			length -= 1
			results.pop(k)