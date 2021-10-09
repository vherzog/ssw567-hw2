# Code Coverage Report
Listed below are the results of running the code coverage analyzer `coverage` on the [Triangle.py](../Triangle.py) python script using the [TestTriangle.py](../TestTriangle.py) `unittest` test cases.

## Run 1
This run was performed before any changes to the code were made. The HTML version of this report can be found [here](./htmlcov1/index.html).
```
$ coverage run TestTriangle.py
Running unit tests
............................
----------------------------------------------------------------------
Ran 28 tests in 0.002s

OK
$ coverage report -m
zsh: correct 'report' to 'reports' [nyae]? n
Name              Stmts   Miss  Cover   Missing

-----------------------------------------------
TestTriangle.py      63      0   100%
Triangle.py          17      0   100%
-----------------------------------------------
TOTAL                80      0   100%
```
