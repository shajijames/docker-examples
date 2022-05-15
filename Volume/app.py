# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:25:38 2022

@author: Shaji
"""

import json

line = open(r'/var/lib/docker/volumes/test_volume/_data/sample.txt').read()
print(line)

try:
    json.loads(line)
    with open(r'/var/lib/docker/volumes/test_volume/_data/sample.json', 'w') as wr:
        wr.write(line)
except Exception as e:
    print("Invalid JSON (or) Error writing to Path ::: "+e)

