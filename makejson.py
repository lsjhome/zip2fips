#!/usr/bin/env python

import json
import re

statecodes = json.load(open('state_fips.json'))
zipmap = {}

for i in range(1,11):
    zfile = open('zipctys/zipcty%d' % i)
    zfile.readline() # skip first line
    for l in zfile:
        m = re.match(r"(?P<zip>.{5}).{18}(?P<state>..)(?P<fips>...)", l)       
        if m:
            r = m.groupdict()
            zipmap[r['zip']] = statecodes[r['state']] + r['fips']

with open('./zip2fips.json', 'w') as fw:
    json.dump(zipmap, fw)
    
with open('./zip2fips.json', 'r') as fr:
    data = json.load(fr)
    print (data)
