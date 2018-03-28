
# Interval

Interval tree implementation in Python.

Interval trees hold intervals in tree structure 
so that overlaps can be observed faster.


## Version
0.1.0

## Python Version
Python 3 is supported. 
Python 3.5.2 is tested on Linux 4.13.0-37-generic #42~16.04.1-Ubuntu.

Python 2 is supported.
Python 2.7.12 is tested on Linux 4.13.0-37-generic #42~16.04.1-Ubuntu.

## Installation

Download this repository.
Use

python setup.py install

or

[sudo] pip install .

to install this module. This module is yet to be added to PyPI.

## Features
- Interval, Node, IntervalTree Structures to encapsulate logic
- Binary Search Tree based IntervalTree structure is default
- Support Node add operation
- Bintrees conditional dependency addition
- Node remove operation
- Python 2 support
- Create setup file
- Overlap check operation
- Adapter classes for bintrees.BinaryTree, bintrees.RBTree, bintrees.AVL 

## TODO
- Create string repr functions for classes
- Make classes pickleable.
- Correct remove bug at root
- Create Strategy pattern for each tree type
- Create StrategyFactory pattern for creating IntervalTrees
- Create examples
- Add example to here.
- Add to github
- CI at Travis
- Create Travis CI script
- Add this module to Python Package Index
- Implement AVL
- Implement RB Tree
- Write further testing

### Python 2 Support

- @property decorator is not the same as Python 3 version syntactically.
This can be solved via deriving classes from object. [DONE]
- Bintrees conditional dependency needs to check 
if bintrees is installed or not. Checking method differs in 
different versions. [DONE]

## Test Results
Ran 19 tests in 0.001s

FAILED (failures=1)

## Coverage

If coverage.py is installed

coverage run tests.py

coverage report --omit=/usr/*

gives coverage results.

Current coverage on Interval is %80.

## Documentation
Documentation can be reached at docs/build/html/index.html.