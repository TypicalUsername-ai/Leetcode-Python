# **LeetCode** python solution tracker #
A self contained, minimal solution tracker for filling leetcode tasks in Python. \
This repo can be freely forked to make individual leetcode solution repositories. \
*For any potential improvements pr's are welcome*

## Set up ##
all the code used to make this tracker work uses pure python and python-included libraries so no futhrer instalation past the python interpreter is required, however it would be best to change the author variable in the **prep** file \
*(Note that this was designed for python 3.10+ so the behaviour for lower versions is untested)*

## Usage ##
1. To begin working on a LeetCode question of choice open the terminal in the main directory and type the following:
```
>> Python prep *your_task_no*
Prepped the init file!
Prepped the solution file!
Prepped the test file!
```
2. This will create a new Solution file in the **Solutions** folder with some boilerplate code, and an addition to the **__init__.py** file there. \
The same will occur in the **Test** folder \
*NOTE: the testing files use the unittest python library, documentation available [here](https://docs.python.org/3/library/unittest.html)*
3. Now the work is up to **You** to fill the boilerplate code with the correct solution \
For the tasks involving data structures you can uncomment the provided line for their implementation from the **Structures** folder
4. The code can be tested with the `Python check *your_task_no*` command \
this will fail the test by default, unless at least one additional user defined test is implemented, as seen below:
```
>> python check 1
testing solution for Lettcode problem 1:
F
======================================================================
FAIL: test_empty (problem_1_test.Problem_1_test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Leetcode_python\Test\problem_1_test.py", line 14, in test_empty
    self.assert_(self.countTestCases() != 1, "no user-implemented testcases!")
AssertionError: False is not true : no user-implemented testcases!

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```


## Happy Coding! ##