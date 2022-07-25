# Arrays
Arrays allow information to be grouped under one identifier. An <span style = "color:lightblue">array</span> is a collection of <span style = "color:lightblue">homogeneous objects</span> (i.e., objects of the same type).
## One-dimensional Arrays
The syntax of initializing an array is shown below. The size of the array must be a positive constant.

```C++
<DATA_TYPE> <ARRAY_NAME> [ <SIZE> ];
```

Each element is stored consecutively in memory and **takes up space** equivalent to the **size of the data type**. Additionally, the syntax of assigning a value at a specified index of an array is shown below.

```C++
<ARRAY_NAME> [ <INDEX ] = <VALUE>;
```

C++ will not complain if the **index is greater than the size of the array** (i.e., index out of bounds). This is a common cause of a <span style = "color:lightblue">run-time segmentation fault error</span>. An out-of-bound array access will return <span style = "color:lightblue">garbage values</span>.

Constant arrays (denoted with `const`) prohibit modification of their elements.

Access to uninitialized elements (i.e., elements with no value stored yet) also return garbage values. Alternatively, an array can be initialized with values.

```C++
<DATA_TYPE> <ARRAY_NAME> [ <SIZE> ] = { <VALUE1>, <VALUE2>, ... };
```

If **not enough values** are specified, the remaining elements are initialized to `0`. If **too many values** are specified, a <span style = "color:lightblue">compilation error</span> occurs. The above syntax can only be used once when the array is first initialized.

## Passing an Array into a Function
The <span style = "color:lightblue">array identifier</span>, its data type, and the size of the array must be passed into the function.

The array is passed by value (i.e., its name → its memory addresss), while its elements are passed by reference. Thus, any changes to the array's elements in the function are permanent.

## Multi-dimensional Arrays
An $N$-dimensional array can be created with the following syntax.

```C++
<DATA_TYPE> <ARRAY_NAME> [ <SIZE1> ] [ <SIZE2> ] ... [ <SIZEN> ];
```

Each element is stored consecutively in memory, where the **last dimension index** `SIZEN` is iterated through first and the **first dimension index** is iterated through last. The array elements are stored in <span style = "color:lightblue">row-major order</span>.

For example, in `int arr[3][5]`, the elements `arr[0][0]` to `arr[0][4]` are iterated through before the first dimension index is incremented (`arr[1][0]`).

Thus, the last dimension index runs the fastest, while the first dimension index runs the slowest.

Both code blocks below are valid multi-dimensional array initialization syntaxes.

```C++
<TYPE> <NAME> [ <SIZE1> ] [ <SIZE2> ] = { { ... }, { ... }, ... };
```

```C++
<TYPE> <NAME> [ <SIZE1> ] [ <SIZE2> ] = { ..., ..., ..., ... };
```
