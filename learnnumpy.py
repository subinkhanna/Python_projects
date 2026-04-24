import numpy as np

## integer  -   int8, int16, int32, int64 
## float    -   float16, float32, float64
## boolean  -   bool_
## string   -   (str_, <U#)
## object   -   (object_)

arr = np.array([1,3,2,4,4], dtype=np.int64) ## int64, int32, int8, int16

print(arr)
print(arr.dtype)
print(f"{arr.nbytes} bytes")

