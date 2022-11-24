# Extract-pairs-that-sum-x
Just having fun with a simple problem and python

## Problem statement
​
This program implements several ways to find all pairs of integers from a list that
sum to a given value. No two numbers in the list are the same. The given list will have at least one number.

List: 3 6 -1 -2 -4 10 -1000 0 23 8 7
Given value X: 6. 
​
The pairs of integers in the list that sum X=12 are:

6 and 0
-2 and 8
-1 and 7

# Python version
Python 3.11.0
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it.
* To run the program via command line with a specific scenario, run for example: `python3 -m app 3,6,-1,-2,-4,10,-1000,0,23,8,7 6`. Take into account that the program start at the `app.py` file, and it takes two arguments, the first is a list of comma separated integers with no duplicates, and the second is the number `x` for which the program should search pairs of integers which sum is `x`.

## Some examples to run:

* `python3 -m app 3,6,-1,-2,-4,10,-1000,0,23,8,7 6`
* `python3 -m app 1,9,5,0,20,-4,12,16,7 12`
* `python3 -m app -1,1 0`
* `python3 -m app 1 1`
* `python3 -m app -1,-2,-3,-4,-5,-6,-7,-8,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-10,-11,-12,-13,-14,0,-15 1`
* `python3 -m app 1,9,21,27,28,30,37,38,39,41,42,47,49,-75,-74,55,59,-69,62,64,-64,-62,67,72,-46,-43,-40,-39,-38,-34,-33,-28,-21,-19,-17,-16,-4,-2 0` wich output should be `21 -21,28 -28,38 -38,39 -39,62 -62,64 -64`
* `python3 -m app 0,5,16,18,22,23,24,25,34,36,37,41,42,47,49,50,54,-67,-66,64,65,67,-57,73,-50,78,-47,-43,-40,-36,-33,-28,-25,-23,-15,-13,-11,-5,-3 15` wich output should be `18 -3,65 -50`

## More test cases from file

There are lots of test cases in the file `test_cases.in` wich corresponding correct ouput obtained via naive O(n^2) algorithm is in the corresponding line of the file `test_cases.out`.

## Many more examples could be generated

Just run `python3 data_for_samples_generator.py` and that script will add more test to the file `test_cases.in` wich corresponding correct ouput obtained via naive O(n^2) algorithm will be added to the file `test_cases.out`.

# Selected solution

There are 4 different solution in the algorithms.py file. All of them tested, but the one selected to solve the problem when running `app.py` is the set based solution, because is considered the simpler one and has a good tradeoff of redeability, complexity and extension in my opinion.

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
