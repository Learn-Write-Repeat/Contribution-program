# Introduction to Numpy

### What is Numpy ?

* Numpy is a python library used for working with arrays.
* It also has functions for working in domain of linear algebra , fourier transform and matrices
* It was created in 2005 by Travis Oliphant as an Open Source Project which means you can use it freely.
* It stands for Numerical-Python

### Why to use Numpy ?

* In python we have lists that serve the purpose of arrays but they are slow to process.
* Numpy aims to provide an array object that is upto 50X faster than the traditional python lists.
* The Array object in numpy is called ndarray.
* Arrays are frequently used in Machine learning and Data-Science , where Speed and Resources are important parmaters.

### Which Language is Numpy written in ?

It is a Python library and is partially written in Python, but **most of the Parts that require fast computation are written in C/C++.**

### Numpy Codebase (Source Code):

[Numpy Source Code](https://github.com/numpy/numpy)

### Installing Numpy 

* You can install it using pip command in terminal as  `pip install numpy`.
* After Installing Numpy, you can import the library by using `import numpy` or `import numpy as np`.
* You can check the version of numpy by `np.__version__`.

### Creating Arrays in Numpy 

```
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])

```

### Array Dimensions

1. 0-D Arrays

```
arr = np.array(42)
```

2. 1-D Arrays

 ```
 arr = np.array([1,2,3,4,5,6,7,8,9,10])
 ```
 
 3. 2-D Arrays
 
 ```
 arr = np.array([[1,2,3,4],[5,6,7,8]])
 ```
 
 4. 3-D Arrays
 ```
 arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
 ```
 
 ### Numpy Array Slicing :
 
 * Slicing in python means taking elements from one given index to another given index.
 * We pass slice instead of index like `[start:end]`
 * We can also define the step like `[start:end:step]`
 * If we don't pass start, start is considered 0
 * If we don't pass end , it is considered as last element of the dimension
 * If we don't pass step, it is considered to be 1
 
 ```
arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr[1:5]
arr[4,:]
arr[:,4]
arr[-3:-1]
arr[::2]
arr[1,2:5]
arr[0:2,1:3]
 ``` 
 ### Data Types in Numpy

* i - Integer
* b - Boolean
* u - Unsigned Integer
* f - Float
* c - Complex Float
* m - Timedelta
* M - Datetime
* O - Object
* S - String 
* U - Unicode String
* V - Fixed chunk of memory for other type

* To Check the datatype of an numpy array, you can use `arr.dtype`

### The Difference Between Copy and View

* The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
* The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
* The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

```
arr1 = np.array([1,2,3,4,5])
x1 = arr1.copy()


arr2 = np.array([6,7,8,9,10])
x2 = arr2.view()
```

### Shape of an array

* The shape of an array is the number of elements in each dimension.
* It can be determined using `arr.shape`
* Integers at every index tells about the number of elements the corresponding dimension has.


### Joining Numpy Arrays

* Joining means putting contents of two or more arrays in a single array.
* In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
* We pass a sequence of arrays that we want to join to the `concatenate()` function, along with the axis. If axis is not explicitly passed, it is taken as 0.

**Example 1**
```
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

```

**Example 2**
```
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
```

### Joining arrays using Stack Functions

* Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
* We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
* We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.


**Example 1**
```
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
```

**Example 2 (Stacking along Rows)**
```
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
```


**Example 3 (Stacking along Columns)**
```
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
```


**Example 4 (Stacking along height)**
```
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))
```



### Splitting Numpy Arrays

* Splitting is reverse operation of Joining.
* Joining merges multiple arrays into one and Splitting breaks one array into multiple.
* We use `array_split()` for splitting arrays, we pass it the array we want to split and the number of splits.

**Example 1**
```
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
```

**Example 2**
```
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)
```

### Numpy Searching Arrays

* You can search an array for a certain value, and return the indexes that get a match.
* To search an array, use the `where()` method.

**Example 1**
```

```

**Example 1**
```
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
```

**Example 2**
```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)
```

**Example 3**
```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)
```

**Example 4 (Search Sorted)**

* There is a method called `searchsorted()` which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

```
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
```


### Numpy Sorting Arrays

* Sorting means putting elements in an ordered sequence
* Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
* The NumPy ndarray object has a function called `sort()`, that will sort a specified array.


**Example 1**
```
arr = np.array([3, 2, 0, 1])
np.sort(arr)
```

**Example 2**
```
arr = np.array(['banana', 'cherry', 'apple'])
np.sort(arr)
```


**Example 3**
```
arr = np.array([True, False, True])
np.sort(arr)
```


**Example 4 (Sorting 2-D Array)**
```
arr = np.array([[3, 2, 4], [5, 0, 1]])
np.sort(arr)
```


### Numpy Filter Array 

* Getting some elements out of an existing array and creating a new array out of them is called filtering.
* In NumPy, you filter an array using a boolean index list.
* If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

**Example 1**
```
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
```

**Example 2**
```
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
```

**Example 3**
```
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

```

### Random Numbers in Numpy

* `from numpy import random`


**Generate Random Number from 0 to 100**
```
x = random.randint(100)
```

**Generate Random Float number between 0 and 1**
```
x = random.rand()
```


**Generate Random Array**
```
x1=random.randint(100, size=(5))
x2=random.randint(100, size=(3, 5))
```



## References:

* [W3schools](https://www.w3schools.com/)










