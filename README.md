
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

to install this module. 

## Features
- Interval, Node, IntervalTree Structures to encapsulate logic
- Binary Search Tree based IntervalTree structure is default
- Support Node add operation
- Bintrees conditional dependency addition
- Node remove operation
- Python 2 support
- Create setup file
- Overlap check operation

## TODO
- Correct remove bug at root
- Adapter classes for bintrees.BST, bintrees.RBT, bintrees.AVL 
- Create examples
- CI at Travis
- Create Travis CI script
- Get coverage tool.
- Meter coverage.
- Implement AVL
- Implement RB Tree
- Write further testing
- Add this module to Python Package Index

### Python 2 Support

- This code does not work on Python 2 because @property
decorator is not the same as Python 3 version syntactically.
This can be solved via deriving classes from object. [DONE]
- Bintrees conditional dependency needs to check 
if bintrees is installed or not. Checking method differs in 
different versions. [DONE]

## Test Results
Ran 14 tests in 0.001s

FAILED (failures=1)