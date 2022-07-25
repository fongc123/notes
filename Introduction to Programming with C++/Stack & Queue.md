# Stack & Queue
<span style = "color:lightblue">Stack</span> and <span style = "color:lightblue">queue</span> are data structures that help manage data more effectively.
## Stack
A stack follows a <span style = "color:lightblue">last-in first-out (LIFO)</span> policy. Here are some common features found in a stack:
- `top()`: get the value of the top item
- `push()`: add a new item to the top
- `pop()`: remove an item from the top

### Example
A sample program that demonstrates a stack implementation.

```C++
// FILE: stack.h
#include <iostream>
#include <cstdlib>
using namespace std;

const int BUFFER_SIZE = 5;

class stack {
	private:
		int data[BUFFER_SIZE];
		int top_index;

	public:
		stack();

		bool empty() const;
		bool full() const;
		int size() const;
		int top() const;

		void push(int);
		void pop();
};
```

- an array is used to store data
- `top_index` is used to monitor the size of the stack and access items
	- `-1`: empty
	- `0`: one item
	- `BUFFER_SIZE - 1`: full
- the stack in this example has a max size of `5`
- functions are first declared in `stack.h` and are defined later in `stack-functions.cpp`
- 
- function explanations
	- `bool empty() const`: check if stack is empty
	- `bool full() const`: check if stack is full
	- `int size() const`: returns the current size of the stack
	- `int top() const`: if not empty, returns the value at the end of the array
	- `void push(int)`: adds a new item to the top of the stack
	- `void pop()`: remove the topmost item of the stack


```C++
// FILE: stack-functions.cpp
#include "stack.h"

stack::stack() { top_index = -1; }

bool stack::empty() const { return (top_index == -1); }

bool stack::full() const { return (top_index == BUFFER_SIZE - 1); }

int stack::size() const { return (top_index + 1); }

int stack::top() const {
	if (!empty()) return data[top_index];

	cerr << "Stack is empty." << endl;
	exit(-1);
}

void stack::push(int x) {
	if (!full()) {
		data[++top_index] = x;
	} else {
		cerr << "Stack is full." << endl;
		exit(-1);
	}
}

void stack::pop() {
	if (!empty()) {
		--top_index;
	} else {
		cerr << "Stack is empty." << endl;
		exit(-1);
	}
}
```

- `::` denotes that the function is part of the class <span style = "color:lightblue">namespace</span>
- `#include` to include the class definition and necessary libraries

> [!INFO]
> In this implementation, old data will still exist in the stack and will only be "removed" when they are replaced by new data.

## Queue
A queue follows a <span style = "color:lightblue">first-in first-out</span> policy. Here are some common features found in a queue:
- `front()`: get the value of the front item
- `enqueue()`: add an item to the back
- `dequeue()`: remove an item from the front

### Example
A sample program that demonstrates a queue implementation.

```C++
// FILE: queue.h
#include <iostream>
#include <cstdlib>
using namespace std;

const int BUFFER_SIZE = 5;

class queue {
	private:
		int data[BUFFER_SIZE];
		int num_items;
		int first;

	public:
		queue();

		bool empty() const;
		bool full() const;
		int size() const;
		int front() const;

		void enqueue(int);
		void dequeue();
};
```

- `num_items` represents the number of items in the queue
- `first` is the index of the item at the front of the queue

```C++
// FILE: queue-functions.cpp
#include "queue.h"

queue::queue() { first = 0; num_items = 0; }

bool queue::empty() const { return (num_items == 0); }

bool queue::full() const { return (num_items == BUFFER_SIZE); }

int queue::size() const { return num_items; }

int queue::front() const {
	if (!empty()) return data[first];

	cerr << "Queue is empty." << endl;
	exit(-1);
}

void queue::enqueue(int x) {
	if (!full()) {
		data[(first + num_items) % BUFFER_SIZE] = x;
		++num_items;
	} else {
		cerr << "Queue is full." << endl;
		exit(-1);
	}
}

void queue::dequeue() {
	if (!empty()) {
		first = (first + 1) % BUFFER_SIZE;
		--num_items;
	} else {
		cerr << "Queue is empty." << endl;
		exit(-1);
	}
}
```

- smart usage of the modulo operator to keep track of `front` while still being able to add more items to the queue

> [!INFO]
> A **circular queue** is shown in this implementation.

