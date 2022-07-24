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
using namespace std;

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
A variable is a <span style = "color:lightblue">named memory location</span> (i.e., a container) for a value to write to, retrieve from, and manipulate. In C++, a variable <u>must</u> be declared and/or defined before it can be used.

It is <span style = "color:lightblue">initialized</span> when a value is assigned to it. If no value is initialized, the initial contents of that variable *may* be garbage.

The computer <span style = "color:lightblue">allocates memory</span> for a variable when it is defined.
> [!INFO]
> Variable declaration ≠ variable definition.

The following code block shows two examples on variable declaration: **single** and **multiple**.

```C++
int radius = 10;

int radius = 10, sum = 0, width = 1;
radius = sum = width + 10;
```

### Example
A sample program that reads two inputs, `x` and `y`, adds them together, and prints the operation in the console.

```C++
#include <iostream>
using namespace std;

int main() {
	int x, y;

	cin >> x;
	cin >> y;

	cout << x << " + " << y << " = " << x + y << endl;

	return 0;
}
```
- sample output: `123 + 456 = 579`
- `cin >> x >> y;` also works
- inputs are separated by **spaces** or **enter**, while extra inputs are ignored

> [!QUESTION]
> What happens when you input non-integer values?

## Operators
Special characters (e.g., `+`, `-`) that perform <span style = "color:lightblue">arithmetic operations</span> on values.

### Modulo
Gets the remainder in an integer division. For example, the remainder of `16 / 5` is `1` or, equivalently, `mod(16, 5) = 1`.

Modulo also supports <span style = "color:lightblue">negative divisors and dividends</span>. It simply follows the following equation and calculates the answer accordingly.
$$
\frac{a}{b}\times b + a \space \% \space b = a
$$
Modulo **does not** support `float` or `double` data types.

### Increment & Decrement
Modifies the operand by a fixed amount.
- <span style = "color:lightblue">pre-increment</span>: modify the operand first, allowing the **result** to be used for further operations (e.g., `++x`)
- <span style = "color:lightblue">post-increment</span>: **current value** is used first for further operations and is only modified later (e.g., `x++`)

The above situations apply for **decrement** (`--`) as well.

### Short-hand Assignment
Simplifies expressions. For example, `n = n + 2` is equivalent to `n += 2`.

### Precedence & Associativity
The following table, obtained from [this link](https://en.cppreference.com/w/cpp/language/operator_precedence), describes operator precedence and associativity in C++.

![[operator-precedence.png|center|600]]

<span style = "color:lightblue">Unary minus</span> negates the value, while subtraction is a simple subtraction. They are not the same.

## Control Statements
To <span style = "color:lightblue">control</span> code, C++ has the following basic control statements.
- if-else
- while loops
- do-while loops
- for loops
- switch

Control statements can be nested within each other.

<span style = "color:lightblue">Switch statements</span> will go through each case until it meets a `break` statement. Typically, a `break` statement is placed inside **each case**. Additionally, switch statements will only allow **integral data types** (e.g., `int`) to be checked. Floating-point data types will not work.

### Loops: Usage Scenarios
Each loop has its own usage scenario.
- for loop: need to count loop iterations
- while loop: unknown number of loop iterations
- do while: code needs to be executed at least once

### Dangling Else
By default, C++ will connect an `else` statement to the closest `if` statement, which may not be intended. Consider the following example.

```C++
int x = 15;

if (x > 20)
if (x > 30)
x = 8;
else
x = 9;
```

The above code block is **equivalent** to the below code block.

```C++
int x = 15;

if (x > 20) {
	if (x > 30)
		x = 8;
	else
		x = 9;
}
```

In both cases, the value of `x` after the program is run is `15`. The second `if` statement will only execute if the first `if` statement is evaluated to `true`.

## User-defined type
An `enum` is a user-defined type that holds a <span style = "color:lightblue">finite</span> set of <span style = "color:lightblue">symbolic (meaningful) objects</span>, making the program easier to understand.

### Declaration
```C++
enum <DATA_TYPE> {
	<NAME1> = <VALUE1>,
	<NAME2> = <VALUE2>,
	...
}
```

`enum` connects meaningful words with integer indices, allowing words to be understood by the program. If a value is not specified, C++ will index the first object as `0` and continue from there.

`enum` types are typically used with switch statements.

### Example
A sample program that defines the user-defined type `shapes`, reads an integer input, and outputs the corresponding shape to the console.

```C++
#include <iostream>
using namespace std;

int main() {
	// shapes (index: 0, 1, 2, 3)
	enum shapes { TEXT, LINE, RECT, CIRCLE };

	int shape;
	cin >> shape;

	// equivalent to comparing integers
	switch (shape) {
		case TEXT:
			cout << "It is a text." << endl;
			break;
		case LINE:
			cout << "It is a line." << endl;
			break;
		case RECT:
			cout << "It is a rectangle." << endl;
			break;
		case CIRCLE:
			cout << "It is a cricle." << endl;
			break;
		default:
			cerr << "No shape." << endl;
			break;
	}

	return 0;
}
```