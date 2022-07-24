# Bitwise Operators
C++ allows the direct modification of the bits of a variable.

## Binary
All information is represented in <span style = "color:lightblue">binary</span>. Each digit represents a <span style = "color:lightblue">bit</span>, and four bits represent a <span style = "color:lightblue">byte</span>. 

For example, `0000 0000 0000 0101` is equal to $1\cdot2^0\space+\space0\cdot2^1\space+\space1\cdot2^2\space+\space0\cdot2^3\space+\space...$ which is equal to `5`.

## Binary Operators
There are operators that modify the bit digits of a value.

| **operator** | **function** | **description** |
|:------------:|:------------:|:---------------:|
|     &     |     `AND`      |      both       |
|      \|      |      `OR`      |  at least one   |
|     ^      |     `XOR`      |    different    |
|     ~      |    `INVERT`    |       not       |
|     <<     |  `SHIFT LEFT`  |   shifts left   |
|     >>     | `SHIFT RIGHT`  |  shifts right   |

A `1` is considered as `true`, while a `0` is considered as `false`. For example, an `AND` will output `1` if and only if both inputs are `1` as well.

### Example
A sample program that modifies the bits of two variables, `x` and `y`, with `int` type.

```C++
#include <iostream>
using namespace std;

int main() {
	unsigned short x = 10;
	unsigned short y = 12;

	// AND
	cout << (x & y) << endl;

	// OR
	cout << (x | y) << endl;

	// XOR
	cout << (x ^ y) << endl;

	// INVERT
	cout << (~ x) << endl;

	// SHIFT LEFT
	cout << (x << 1) << endl;

	// SHIFT RIGHT
	cout << (x >> 1) << endl;

	return 0;
}
```
- binary representation of variables `x` and `y`
		- `10`:  `0000 0000 0000 1010`
		- `12`: `0000 0000 0000 1100`
- output of each operation
	- `AND`: `0000 0000 0000 1000` (`8`)
	- `OR`: `0000 0000 0000 1110` (`14`)
	- `XOR`: `0000 0000 0000 0110` (`6`)
	- `INVERT`: 