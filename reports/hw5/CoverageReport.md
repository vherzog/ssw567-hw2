# Code Coverage Report
Listed below are the results of running the code coverage analyzer `coverage` on the [triangle.py](../triangle.py) python script using the [test_triangle.py](../test_triangle.py) `unittest` test cases.

Detailed reports on this repo's code coverage can also be found [on Codecov.io](https://app.codecov.io/gh/vherzog/ssw567-hw2).

## Run 1
This run was performed before any changes to the code were made.
```
coverage run -m unittest TestTriangle
Running unit tests
............................
----------------------------------------------------------------------
Ran 28 tests in 0.002s

OK
$ coverage report -m
Name              Stmts   Miss  Cover   Missing

-----------------------------------------------
test_triangle.py      63      2    97%   105-106
triangle.py          17      0   100%
-----------------------------------------------
TOTAL                80      2    98%
```

## Run 2
After running a static code analysis ([see report here](./StaticAnalysisRuns.md)) and making the required changes, the code coverage results returned:
```
$ coverage run -m unittest TestTriangle
$ coverage report -m
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
test_triangle.py      36      1    97%   121
triangle.py           21      0   100%
------------------------------------------------
TOTAL                 57      1    98%
```

## Run 3
I realized, by running the test_triangle script using `coverage`, I did not need the `if __name__ == '__main__':` statement. After removing this, I got to **100%** code coverage.
```
$ coverage run -m unittest TestTriangle
$ coverage report -m
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
test_triangle.py      44      1    98%   158
triangle.py           21      0   100%
------------------------------------------------
TOTAL                 65      1    98%
```
