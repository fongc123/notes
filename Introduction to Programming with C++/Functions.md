# Functions
Functions make programs easier to read and to write.

## Basics
### Function Definition
All definitions need a <span style = "color:lightblue">return type</span>, a function name, a set of parameters, and a body.

```C++
<RETURN_TYPE> <FUNCTION_NAME> (<PARAMETERS>) { <FUNCTION_BODY> }
```

The function must return an output that matches the denoted return type. Additionally, the data type of each parameter must also be specified.

### Function Call
In a function call, the function name and a set of parameters specified.

```C++
<FUNCTION_NAME> (<PARAMETERS>)
```

### Example
A sample program that defines the function `max()` which will return the greater value between two integer inputs.

```C++
#include <iostream>
using namespace std;

int max(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}

int main() {
	cout << max(5, 10) << endl;

	return 0;
}
```

If data types don't match, an error will occur.

## About Functions
The `main()` function is reserved. The command interpreter of the operating system (i.e., the <span style = "color:lightblue">shell</span>) looks for the `main()` function and starts the execution from there.

The <span style = "color:lightblue">formal parameter list</span> is the list of parameters in the function definition, while the <span style = "color:lightblue">actual parameter list</span> is the list of arguments that are <u>passed into</u> the function when the function is called. The number and order of the parameters in both the formal parameter list and the actual parameter list *must* match.

### `return` keyword
All functions, through the `return` keyword, generally return <span style = "color:lightblue">an object</span> which may be:
- a <span style = "color:lightblue">signal</span>: did the function run as expected? [^1]
- a <span style = "color:lightblue">result</span> from computation
- a <span style = "color:lightblue">new object</span> (e.g., a window)

Functions **cannot** return arrays. Instead, a function can return **a pointer to an array** (*see Pointers*).

If the function is expected to <span style = "color:lightblue">return nothing</span>, the `void` keyword is specified as the return type.

### Benefits of Modular Programming
A common approach to solve complex problems is to **divide and conquer** the program into smaller modules.
- easier to understand
- easier to modify
- reusable code

## Passing Parameters
How are values <u>inputted</u> into functions?

### Pass-by-value (PBV)
Only the **values** of the actual parameters are copied into the formal parameters of the function.
- the value of the actual parameter is not changed when passed
- new memory is allocated for the copied parameters

### Reference Variables
An <span style = "color:lightblue">alias</span>, which is denoted by the `&` symbol before the variable name, of another variable.
- reference variables use the same memory space as the original variable
- changing the reference variable changes the original variable

### Pass-by-reference (PBR)
The values of the actual parameters are not copied.
- the formal parameters become the <span style = "color:lightblue">reference variable</span> of the actual parameters
- the function will change the value of the actual parameter



[^1]: In `int main()`, `return 0` means the function worked, while `return 1` means the function failed.