# File Input & Output
A <span style = "color:lightblue">stream</span> is a sequence of characters. A <span style = "color:lightblue">stream object</span> is used to convert **input and output data** into **a sequence of data**.

The library `iostream` combines the `istream` (*dealing with input*) and `ostream` (*dealing with output*) <span style = "color:lightblue">header files</span>.
- `istream cin`: standard input
- `ostream cout`: standard output
- `ostream cerr`: standard error output

The library `fstream` containts `ifstream` and `ofstream` for input and output from a file.

An <span style = "color:lightblue">input file</span> must exist before any input can be read. An <span style = "color:lightblue">output file</span> will be automatically created and **will erase and overwrite** any pre-existing output file with the same filename.

## Reading In
The sample code block below reads in each line of a file titled `input.txt` and outputs it to the standard output.
```C++
#include <fstream>
#include <iostream>
using namespace std;

int main() {
	ifstream ifs("input.txt");
	string line;

	if (ifs) {
		while (true) {
			getline(ifs, line);
	
			if (ifs.eof()) break;
	
			cout << line << endl;
		}
	
		ifs.close();
	}

	return 0;
}
```
- `ifstream ifs`: file input object for reading in a file
- `if (ifs)`: checks for any errors when reading in a file (returns `true` if none and `false` otherwise)
- `ifs.eof()`: signals the end of the file

> [!INFO]
> If `ifs.eof()` is not included, `ifs` will continue to read in blank lines indefinitely.

## Writing Out
The sample code block below writes `"hello"` out to a file titled `output.txt`.

```C++
#include <fstream>

int main() {
	ofstream ofs("output.txt");

	ofs << "hello" << endl;

	ofs.close();

	return 0;
}
```

> [!INFO]
> To ***append*** to an existing file, use `ofstream ofs("output.txt", ios_base::app)` instead.

## Input
When inputting from the console with `cin`, all white spaces (`' '`, `'\t'`, `'\n'`) will be skipped. The input can read in a single character or a sequence of characters (i.e., array), as shown below.

```C++
char x; cin >> x;
```

```C++
char x[20]; cin >> x;
```

### Functions
There are special functions in C++ for reading in inputs as well.
- `cin.getline(char s[], int max-num-char, char terminator)` continuously reads in characters until one of the following conditions is met:
	- a number of `max-num-char - 1` characters are read in
	- a `terminator` character is found (*not read in*)
- `getline(cin, s, 'X')` reads in a line until a new line or a delimitter character is met