import numpy as np

## integer  -   int8, int16, int32, int64 
## float    -   float16, float32, float64
## boolean  -   bool_
## string   -   (str_, <U#)
## object   -   (object_)

#    arr = np.array([1,3,2,4,4], dtype=np.int64) ## int64, int32, int8, int16

#    print(arr)
#    print(arr.dtype)
#    print(f"{arr.nbytes} bytes")

#    print(np.__version__)

#my_list = [1,2,3,4,5]

#print(my_list)

#nparray = np.array(my_list)
#print(nparray)

#print(type(nparray))

#nparray = nparray * 2
#print(nparray)
#print(nparray.ndim)

#my_list = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

#nparray = np.array(my_list)

#print(nparray.ndim)
#print(nparray.shape)

#scores = np.array([90, 50, 67, 88, 50, 89])
#print(scores <  60)
#scores[scores <  60] = 0
#print(scores)


#my_list = [[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]],
#           [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]],
#           [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]]

#multidimarr = np.array(my_list)
#print(multidimarr.shape)

#print(multidimarr < 3)

##multi-dimension indexing vs chain indexing

#print(multidimarr[0][1][2]) ##Chain-dimensional indexing

#print(multidimarr[0, 2, 0]) ##multi-dimensional indexing


my_list = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

nparray = np.array(my_list)

#print(nparray[0:2, 2:]) ## Slicing  

##Arithmetic : Scalar, Vector

#print(nparray + 1)
#print(nparray * 15)
#print(nparray - 12)
#print(nparray / 3)
#print(nparray ** 1.5)

##Vector is a single dimension - such as 1D list
## Scalar is a single value


#print(np.sqrt(nparray))  ##np.round(nparray), np.ceil(arr), np.floor(arr), np.pi (pie)

#radii = np.pi * (nparray **2)
#print(radii)

##Element-wise arithmetic

nparray2 = nparray * 4
#print(nparray + nparray2) ## arr1+arr2, arr1-arr2, arr1*arr2, arr1/arr2, arr1**arr2

print(np.sum(nparray2)) #np.mean, np.std, np.var (variance), np.min, np.max, np.argmin(array) - Position of arg of min value
# np.argmax  <- index of max value

print(nparray2)

#print(np.sum(nparray2, axis=0))    ##axis = 0 - Sum of values in column, axis=1, sum of values in a row

##Where clause retains the original shape of array
np.where(nparray2 > 2.5, nparray2, -1)  ## cond, array, fill value (values to be filled for items that do not satisfy condition)




