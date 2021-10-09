# Static Code Analysis Report
Listed below are the results of running the static code analyzer `pylint` on the [Triangle.py](../Triangle.py) python script.

## Run 1:
```
$ pylint Triangle.py
************* Module Triangle
Triangle.py:50:0: C0301: Line too long (115/100) (line-too-long)
Triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:0: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:50:4: R1705: Unnecessary "elif" after "return" (no-else-return)

Triangle.py:12:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 5.00/10 (previous run: 5.00/10, +0.00)
```
