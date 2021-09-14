# Test Report
This test report contains the results of running TestTriangle on the original (buggy) [Triangle.py](../Triangle.py) code.

| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| testInvalidFloatInputA | (10.0,7,4) | InvalidInput | InvalidInput | Pass |
| testInvalidFloatInputB | (10,'7',4) |  InvalidInput | InvalidInput  | Pass |
| testInvalidFloatInputC | (10,7,'4') |  InvalidInput | InvalidInput  | Pass |
| testInvalidOverMaxInputA | (201,200,200) |  InvalidInput | InvalidInput  | Pass |
| testInvalidOverMaxInputB | (200,201,200) |  InvalidInput | InvalidInput  | Pass |
| testInvalidOverMaxInputC | (200,200,201) |  InvalidInput | InvalidInput  | Pass |
| testInvalidStringInputA | ('10',7,4) | InvalidInput | ERROR | Fail |
| testInvalidStringInputB | (10,'7',4) | InvalidInput | ERROR | Fail |
| testInvalidStringInputC | (10,7,'4') | InvalidInput | ERROR | Fail |
| testInvalidSumSidesA | (10,7,2) |  InvalidInput | InvalidInput  | Pass |
| testInvalidSumSidesB | (7,10,2) |  InvalidInput | InvalidInput  | Pass |
| testInvalidSumSidesC | (7,2,10) |  InvalidInput | InvalidInput  | Pass |
| testInvalidUnderMinInputA | (0,1,1) |  InvalidInput | InvalidInput  | Pass |
| testInvalidUnderMinInputB | (1,0,1) |  InvalidInput | InvalidInput  | Pass |
| testInvalidUnderMinInputC | (1,1,0) |  InvalidInput | InvalidInput  | Pass |
| testValidEquilateralTriangles | (1,1,1) | Equilateral | InvalidInput | Fail |
| testValidIsoscelesTriangleA | (3,2,2) | Isosceles | InvalidInput | Fail |
| testValidIsoscelesTriangleB | (2,3,2) | Isosceles | InvalidInput | Fail |
| testValidIsoscelesTriangleC | (2,2,3) | Isosceles | InvalidInput | Fail |
| testValidRightTriangleA | (3,4,5) | Right | InvalidInput | Fail |
| testValidRightTriangleB | (5,3,4) | Right | InvalidInput | Fail |
| testValidRightTriangleC | (4,5,3) | Right | InvalidInput | Fail |
| testValidScaleneTriangleA | (4,6,9) | Scalene | InvalidInput | Fail |
| testValidScaleneTriangleB | (9,4,6) | Scalene | InvalidInput | Fail |
| testValidScaleneTriangleC | (6,9,4) | Scalene | InvalidInput | Fail |
| testValidSumSidesA | (10,7,4) | Scalene | InvalidInput | Fail |
| testValidSumSidesB | (7,10,4) | Scalene | InvalidInput | Fail |
| testValidSumSidesC | (7,4,10) | Scalene | InvalidInput | Fail |
