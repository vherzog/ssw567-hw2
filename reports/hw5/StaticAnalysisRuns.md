# Static Code Analysis Report
Listed below are the results of running the static code analyzer `pylint` on the [Triangle.py](../Triangle.py) python script.

## Run 1:
This run was performed before any changes were made to the original code.
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
```
$ pylint TestTriangle.py
************* Module TestTriangle
TestTriangle.py:39:0: C0301: Line too long (108/100) (line-too-long)
TestTriangle.py:42:0: C0301: Line too long (108/100) (line-too-long)
TestTriangle.py:45:0: C0301: Line too long (108/100) (line-too-long)
TestTriangle.py:48:0: C0301: Line too long (102/100) (line-too-long)
TestTriangle.py:51:0: C0301: Line too long (102/100) (line-too-long)
TestTriangle.py:54:0: C0301: Line too long (102/100) (line-too-long)
TestTriangle.py:1:0: C0103: Module name "TestTriangle" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:17:0: C0115: Missing class docstring (missing-class-docstring)
TestTriangle.py:20:4: C0103: Method name "testInvalidStringInputA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:20:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:23:4: C0103: Method name "testInvalidStringInputB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:26:4: C0103: Method name "testInvalidStringInputC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:29:4: C0103: Method name "testInvalidFloatInputA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:32:4: C0103: Method name "testInvalidFloatInputB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:35:4: C0103: Method name "testInvalidFloatInputC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:38:4: C0103: Method name "testInvalidOverMaxInputA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:41:4: C0103: Method name "testInvalidOverMaxInputB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:44:4: C0103: Method name "testInvalidOverMaxInputC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:44:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:47:4: C0103: Method name "testInvalidUnderMinInputA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:50:4: C0103: Method name "testInvalidUnderMinInputB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:50:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:53:4: C0103: Method name "testInvalidUnderMinInputC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:53:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:56:4: C0103: Method name "testInvalidSumSidesA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:59:4: C0103: Method name "testValidSumSidesA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:62:4: C0103: Method name "testInvalidSumSidesB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:65:4: C0103: Method name "testValidSumSidesB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:68:4: C0103: Method name "testInvalidSumSidesC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:68:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:71:4: C0103: Method name "testValidSumSidesC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:71:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:74:4: C0103: Method name "testValidEquilateralTriangles" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:74:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:77:4: C0103: Method name "testValidRightTriangleA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:77:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:80:4: C0103: Method name "testValidRightTriangleB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:80:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:83:4: C0103: Method name "testValidRightTriangleC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:83:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:86:4: C0103: Method name "testValidScaleneTriangleA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:89:4: C0103: Method name "testValidScaleneTriangleB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:89:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:92:4: C0103: Method name "testValidScaleneTriangleC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:92:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:95:4: C0103: Method name "testValidIsoscelesTriangleA" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:95:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:98:4: C0103: Method name "testValidIsoscelesTriangleB" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:98:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:101:4: C0103: Method name "testValidIsoscelesTriangleC" doesn't conform to snake_case naming style (invalid-name)
TestTriangle.py:101:4: C0116: Missing function or method docstring (missing-function-docstring)
TestTriangle.py:17:0: R0904: Too many public methods (28/20) (too-many-public-methods)

--------------------------------------------------------------------
Your code has been rated at -0.48/10 (previous run: -0.48/10, +0.00)
```
