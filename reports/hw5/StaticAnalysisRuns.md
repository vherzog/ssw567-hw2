# Static Code Analysis Report
Listed below are the results of running the static code analyzer `pylint` on the [triangle.py](../triangle.py) python script.

## triangle.py
### Run 1
This run was performed before any changes were made to the original code.
```
$ pylint triangle.py
************* Module Triangle
triangle.py:50:0: C0301: Line too long (115/100) (line-too-long)
triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name)
triangle.py:12:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name)
triangle.py:12:0: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
triangle.py:12:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
triangle.py:12:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
triangle.py:50:4: R1705: Unnecessary "elif" after "return" (no-else-return)

triangle.py:12:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 5.00/10 (previous run: 5.00/10, +0.00)
```

## Run 2
```
$ pylint triangle.py
************* Module Triangle
triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)

triangle.py:13:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 6.25/10 (previous run: 6.25/10, +0.00)
```

### Run 3
```
$ pylint triangle.py
************* Module triangle
triangle.py:13:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)

triangle.py:13:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
triangle.py:13:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 6.88/10 (previous run: 6.88/10, +0.00)
```

### Run 4
```
$ pylint triangle.py
************* Module triangle
triangle.py:12:0: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)

triangle.py:12:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
triangle.py:12:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
triangle.py:12:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 7.50/10, +0.00)
```

### Run 5
```
$ pylint triangle.py
************* Module triangle
triangle.py:12:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 9.38/10 (previous run: 9.38/10, +0.00)
```

### Run 6
```
$ pylint triangle.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## test_triangle.py
### Run 1
```
$ pylint test_triangle.py
************* Module TestTriangle
test_triangle.py:39:0: C0301: Line too long (108/100) (line-too-long)
test_triangle.py:42:0: C0301: Line too long (108/100) (line-too-long)
test_triangle.py:45:0: C0301: Line too long (108/100) (line-too-long)
test_triangle.py:48:0: C0301: Line too long (102/100) (line-too-long)
test_triangle.py:51:0: C0301: Line too long (102/100) (line-too-long)
test_triangle.py:54:0: C0301: Line too long (102/100) (line-too-long)
test_triangle.py:1:0: C0103: Module name "TestTriangle" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:17:0: C0115: Missing class docstring (missing-class-docstring)
test_triangle.py:20:4: C0103: Method name "testInvalidStringInputA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:23:4: C0103: Method name "testInvalidStringInputB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:26:4: C0103: Method name "testInvalidStringInputC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:29:4: C0103: Method name "testInvalidFloatInputA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:32:4: C0103: Method name "testInvalidFloatInputB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:35:4: C0103: Method name "testInvalidFloatInputC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:38:4: C0103: Method name "testInvalidOverMaxInputA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:41:4: C0103: Method name "testInvalidOverMaxInputB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:44:4: C0103: Method name "testInvalidOverMaxInputC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:44:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:47:4: C0103: Method name "testInvalidUnderMinInputA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:50:4: C0103: Method name "testInvalidUnderMinInputB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:50:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:53:4: C0103: Method name "testInvalidUnderMinInputC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:53:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:56:4: C0103: Method name "testInvalidSumSidesA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:59:4: C0103: Method name "testValidSumSidesA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:62:4: C0103: Method name "testInvalidSumSidesB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:65:4: C0103: Method name "testValidSumSidesB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:68:4: C0103: Method name "testInvalidSumSidesC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:68:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:71:4: C0103: Method name "testValidSumSidesC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:71:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:74:4: C0103: Method name "testValidEquilateralTriangles" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:74:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:77:4: C0103: Method name "testValidRightTriangleA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:77:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:80:4: C0103: Method name "testValidRightTriangleB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:80:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:83:4: C0103: Method name "testValidRightTriangleC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:83:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:86:4: C0103: Method name "testValidScaleneTriangleA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:89:4: C0103: Method name "testValidScaleneTriangleB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:89:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:92:4: C0103: Method name "testValidScaleneTriangleC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:92:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:95:4: C0103: Method name "testValidIsoscelesTriangleA" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:95:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:98:4: C0103: Method name "testValidIsoscelesTriangleB" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:98:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:101:4: C0103: Method name "testValidIsoscelesTriangleC" doesn't conform to snake_case naming style (invalid-name)
test_triangle.py:101:4: C0116: Missing function or method docstring (missing-function-docstring)
test_triangle.py:17:0: R0904: Too many public methods (28/20) (too-many-public-methods)

--------------------------------------------------------------------
Your code has been rated at -0.48/10 (previous run: -0.48/10, +0.00)
```
