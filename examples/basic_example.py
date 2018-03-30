import intervalt
# import numpy as np 
from random import randrange

vals = [(randrange(0,10),randrange(11,20)) for i in range(10)]
intervals = [intervalt.Interval(i[0],i[1]) for i in vals]
nodes = [intervalt.Node(i) for i in intervals]

tree = intervalt.IntervalBSTree(nodes[0])

for node in nodes[1:]:
    tree.add(node)
print(tree.check_overlap(intervalt.Interval(0,10)))