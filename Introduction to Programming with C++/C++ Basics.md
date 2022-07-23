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
These are libraries that come with C++. The `iostream` library (*used in the above example*) is a standard C++ library.