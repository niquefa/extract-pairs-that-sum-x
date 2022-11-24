# extract-pairs-that-sum-x
Just having fun with a simple problem and python

## Problem statement
​
This program implements several ways to find all pairs of integers from a list that
sum to a given value. No two numbers in the list are the same. The given list will have at least one number.

List: 3 6 -1 -2 -4 10 -1000 0 23 8 7
Given value X: 6
​
The pairs of integers in the list that sum X=12 are:

6 and 0
-2 and 8
-1 and 7

# Python version
Python 3.11.0
​
## Running locally

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To locally start the service: `: ./run.sh`


# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.