# Pointer
<span style = "color:lightblue">Pointers</span> are addresses to other variables. A variable name is a symbolic name given to some storage location in the memory. A <span style = "color:lightblue">literal constant</span> is the value assigned to or stored in the variable.

## `lvalue` & `rvalue`
A variable has two roles:
- `lvalue`: location in memory of the variable (*read-write*)
- `rvalue`: value in storage (*read only*)

### Example: Pre-increment and post-increment
The pre-increment operator (`++x`) is incremented first before it is returned.
1. The variable `x` is passed in by reference.
2. It is incremented by `1`.
3. The increment returns `x` by reference.

Here, the returned output is the `lvalue` of `x`, as the output is the current value stored in the storage location of `x`.

On the other hand, the post-increment operator (`x++`) is returned first before it is incremented.
1. The variable `x` is passed in by reference.
2. The **current value** is saved.
3. The variable is incremented by `1`.
4. The saved value of `x` is returned by value.

Here, the returned output is the `rvalue` of `x`.

## Pointer Operations
Listed below are common operators related to addresses and pointers.
- `&`: get the address of a variable
- `int* x`: creates an `int` pointer (*doesn't point to anything yet*)
- `*x`: dereference operator to get the `rvalue` of the memory location that the pointer `x` is pointing to
- `sizeof()`: size of the data type

## `const` objects & `const` pointers
When a `const` object is created, C++ doesn't allow modification of the object. On the other hand, when a `const` pointer is created, the pointer will only point to the same memory location.

- `int* p`: no restrictions
- `const int* p`: restrict changing object, but pointer can point to other addresses
- `int* const p`: restrict changing pointer, but changing object is possible
- `const int* const p`: all restrictions

