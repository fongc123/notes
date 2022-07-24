# Random Numbers
Random numbers cannot be truthfully generated in C++ or in any programming language. Instead, pseudorandom numbers are generated based on a seed.

## How to generate **pseudorandom** numbers?
The `time.h` library is used to use the current time as the seed. If the same seed is used, the same set of random numbers will be generated.
```C++

#include <iostream>
#include <time.h>

int main() {
	srand(time(0));

	int range = 20;
	int start = 5;
	cout << rand() % range + 20 << endl;

	return 0;
}

```

The above code block generates pseudorandom numbers between 5 and 25 (`start` is `5` and `range` is `20`).

> [!INFO]
> `rand()` generates pseudorandom numbers.

