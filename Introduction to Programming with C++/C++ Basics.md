# Basics
Here are some <span style = "color:lightblue">rules & guidelines</span> that are applicable to any C++ program.
- all programs can be compiled and run in a terminal
- all C++ statements end with a `;`
	- `//` for single line comments
	- `/*` and `*/` for multi-line comments
- extra spaces and new lines do not interfere with the compiler, but adequate spacing improves readability
- special characters:
	- `\t`: tab
	- `\b`: backspace
	- `\n`: new line
	- `\0`: null character
- case-sensitive
## Hello, world!
A <span style = "color:lightblue">program</span> consists of statements. A <span style = "color:lightblue">statement</span> consists of <span style = "color:lightblue">expressions</span>.
- a logical expression: `x > y`
- an arithmetic expression: `5 + 4`

Here is a simple program that prints `'hello world'` in the console.
```C++
#include <iostream>
using namspace std;

int main() {
	cout << "hello world" << endl;

	return 0;
}
```
- `using namespace std`: standard C++ namespace (*more later*)
- `return 0`: "nice ending"
- `endl`: ends the current line and creates a new line (*basically `\n`*)

## Entry Point
Every program must have <u>one and only one</u> `main()` function.
```C++
int main() { ... }
```
```C++
int main(int argc, char** argv) { ... }
```
These two `main()` functions serve the same purpose; however, the former is a **simplified form**, while the latter is the **general form**.

## Libraries
<span style = "color:lightblue">Libraries</span> are a collection of sub-programs, which are equivalent to <span style = "color:lightblue">classes</span>. The `#include` keyword must be used, typically in the beginning of the file, to reference the library.

### Standard C++ Libraries
These are libraries that come with C++. Standard libraries **do not need a file suffix** and **are denoted with `<` and `>`**. The `iostream` library (*used in the above example*) is a standard C++ library that deals with input and output (I/O).
- `cin`: standard input stream → object to read (e.g., keyboard, file)
- `cout`: standard output stream → object to print (e.g., screen, file)
- `cerr`: standard error stream → object to print error message
- `clog`: standard output stream for logging

### User-defined Libraries
You can also define your own libraries. Self-created libraries **must have a suffix as either `.h` or `.hpp`** and **are denoted with double quotation marks (`"`)**.

## Storing Data
### Base 2
A computer uses <span style = "color:lightblue">binary numbers</span> to represent data.
- only two possibilities: `0` or `1`
- a <span style = "color:lightblue">binary digit</span> is a <span style = "color:lightblue">bit</span>
- one <span style = "color:lightblue">byte</span> is eight bits

The <span style = "color:lightblue">maximum N-digit number</span> in base 2 is $2^{N} - 1$.

### Characters
One character represents one byte (*more data types below*). The <span style = "color:lightblue">American Standard Code for Information Interchange (ASCII)</span> is the encoding scheme to convert 8-bit integers to characters. In C++, characters can be *operated* on, as they are represented by numbers. For example, `'a'` is represented by a `1`, while `'b'` is represented by a `2`. Thus, this expression is valid: `'a' + 'b' = 3`.

## Data Types
As with other OOP programing languages, C++ has various <span style = "color:lightblue">data types</span>. The larger the size that the data types use, the more data (i.e., longer numbers) they can store.

| **type**  | **keyword** | **size (32-bit)** | **size (64-bit)** | **example** |
|:---------:|:-----------:|:-----------------:|:-----------------:|:-----------:|
|  Boolean  |   `bool`    |         1         |         1         |   `true`    |
| Character |   `char`    |         1         |         1         |    `'a'`    |
|  Integer  |    `int`    |         4         |         4         |    `40`     |
|   Short   |   `short`   |         2         |         2         |      -      |
|   Long    |   `long`    |         4         |         8         |      -      |
|   Float   |   `float`   |         4         |         4         |    `2.2`    |
|  Double   |  `double`   |         8         |         8         |      -      | 

- more bytes mean more numbers represented (*higher precision*)
- a <span style = "color:lightblue">32-bit machine</span> uses CPUs where the <span style = "color:lightblue">data bus width</span> and <span style = "color:lightblue">memory address width</span> are 32 bits (*likewise for 64-bit machine*)
- <span style = "color:lightblue">signed</span> vs. <span style = "color:lightblue">unsigned</span> integer data
	- signed: represents <u>both positive and negative</u> integers
	- unsigned: <u>only positive</u> integers
- other data types
	- `string`: sequence of `char` but is not a basic data type
	- `long long`
	- `long double`

## Type Conversion
When performing operations, data types must match each other.

### Automatic Conversion
<span style = "color:lightblue">Coercion</span> is the automatic conversion of data types in an operation (e.g., an addition operation).
- `int` + `double` → `double` + `double`
- `char` + `char` → `int` + `int` (*ASCII representation*)

Converting from a high precision type to a low precision type causes loss of data. The extra information is not approximated but instead **truncated**.

### Manual Conversion
<span style = "color:lightblue">Casting</span> manually changes the data type and, thus, the value temporarily.
```C++
float x = 10.595;        // value of x: 10.595

x = static_cast<int>(x); // value of x: 10
```

## Variables
A variable is a <span style = "color:lightblue"