#!python3

from collections import defaultdict

def dv():
    return "My default"

d = defaultdict(dv)

d["A"] = "some"
d["B"] = "some 2"

print(d["A"])