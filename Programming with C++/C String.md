# C String
In C++, <span style = "color:lightblue">strings</span> have their own <span style = "color:lightblue">class</span> and are part of the `cstring` library. Strings are not a basic data type. Although they are represented as **an array of characters**, a simple `char` array is different from a C string.

## Representation
Strings are represented by a one-dimensional character array where the last element is a <span style = "color:lightblue">null character</span> `'\0'`. For example, the string `"hello"` is represented by an array containing the characters `'h'`, `'e'`, `'l'`, `'l'`, `'o'`, and `'\0'` in order.

Since each `char` is stored in a cell in the array, a string with size $N$ is stored in a `char` array of size $N+1$. 

```C++
#include <iostream>
using namespace std;

int main() {
	char s[6] = { 'h', 'e', 'l', 'l', 'o', '\0' };
	
	cout << s << endl;

	return 0;
}
```

Typically, when the name of array is printed to the console, the array's **memory address** will be printed instead of the array's contents. However, the above code block will print the string instead of the memory address.

```C++
#include <iostream>
using namespace std;

int main() {
	int counter = 0;
	char s[6] = { 'h', 'e', 'l', 'l', 'o', '\0' };

	for (int i = 0; s[i] != '\0'; ++i) counter++;
	
	cout << counter << endl;

	return 0;
}
```

When looping through a string, the length of the string is not needed, as only the presence of the null character `'\0'` indicates the end of the string.

## Useful Functions
Some useful functions for string manipulation are shown below.
- `string s`: creates an empty string
- `string s(3, 'A')`: creates three copies of `'A'`, resulting in `AAA`
- `s1 + s2`: concatenates the two strings
- `s1.compare(s2)`: compares the two strings
	- `0`: if the strings are the same
	- `1`: if `s1` is lexicographically greater than `s2`
	- `2`: if `s1` is lexicographically less than `s2`
- `s.substr(j, N)`: returns the substring that starts from index `j` and that consists of `N` characters
- `s1.find(s2, j)`: finds the index of `s2` in `s1` starting from index `j`
	- if `s2` is not found, it will return a constant `string::npos` which is the max `unsigned int`
- `s1.rfind(s2, j)`: same as previous but in reverse
- `s1.replace(j, N, s2)`: replaces a substring in `s1` that starts at index `j` and that consists of `N` characters with `s2`

### `replace()` Example
A sample program that showcases the string `replace()` function.
```C++
#include <iostream>
using namespace std;

int main() {
	string s = "hello world";
	s.replace(0, 10, "ok");

	cout << s << endl;

	return 0;
}
```

The substring of `s` that starts at index `0` and that consists of `10` characters is `"hello worl"` which is replaced by `"ok"`. Thus, the value of `s` after the program is run is `"okd"`. 