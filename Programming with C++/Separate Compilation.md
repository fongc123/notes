# Separate Compilation
Instead of having all the code in one file, parts can be divided into multiple files, compiled, and run as one single <span style = "color:lightblue">executable program</span>.

All global functions, variables, local functions that are used in the **main file** but are defined in a **separate file** must be first **declared** in the original file.
- <span style = "color:lightblue">global constants</span>: repeat their definition
- <span style = "color:lightblue">external variables</span>: specified with keyword `extern`
- <span style = "color:lightblue">external functions</span>: function declaration with keyword `extern` (*optional*)

The keyword `extern` before a variable name denotes that the variable is global and is defined in another file. Functions do not *need* the `extern` keyword, as functions are global regardless.

A variable can be declared many times but can only be defined once even if it's in another file.

A <span style = "color:lightblue">function declaration</span> lets the compiler know that the function is defined elsewhere but is to be used now.

## Procedure
Compilation is done with the command line, where <span style = "color:lightblue">object files</span> (files with `.o` suffix) are created from <span style = "color:lightblue">source files</span> (files with `.cpp` suffix). Suppose our project has three files: `main.cpp`, `file1.cpp`, and `file2.cpp`.

1. Run the following to compile **all files**.
   ```bash
   g++ -o run main.cpp file1.cpp file2.cpp
	```
1. **OR** separately compile each one and link them together.
   ```bash
   g++ -c main.cpp
   g++ -c file1.cpp
   g++ -c file2.cpp
   g++ -o run main.o file1.o file2.o
	```
1. Run `./run` to run the executable program named `run`.

If changes are made to only **one file**, it is not necessary to compile **all files** again. Compile the `.cpp` file with changes and link the `.o` file to the other `.o` files again.

## Header Files
Header files contain the <span style = "color:lightblue">definitions of global variables and constants</span> and the <span style = "color:lightblue">declarations of global variables and functions</span>. With header files, definitions and declarations do not have to be repeated when creating a new `.cpp` file.

A user-created header file has the `.h` file extension. To include the file in a program, use the `#include` keyword.

```C++
#include "header.h"
```

Unlike standard C++ libraries, quotation marks are used instead.

Below are some header files of standard C++ libraries.
- `iostream`: input and output
- `iomanip`: input and output manipulation
- `cctype`: character functions (e.g., `isdigit(char)`, `isspace(char)`, `issuper(char)`)
- `cstring`: C string
- `cmath`: math functions
- `cstdlib`: commonly used functions

