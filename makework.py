#!/usr/bin/env python

from tasks import available
import simplejson as json
from StringIO import StringIO

results = {}
lines = [line.strip() for line in open('tld.txt')]
for tld in lines:
	results[tld] = available.delay("arnoudvermeer", tld)

length = len(results.keys())
io = StringIO()
j = {}

while length > 0:
	for k in results.keys():
		result = results[k]
		if result.ready():
			try:
				j[k] = result.get(timeout=1)
				json.dump(j, io)
			except:
				pass
			length -= 1
			results.pop(k)
			print io.getvalue()
			io.truncate(0)
			j.pop(k)
			
