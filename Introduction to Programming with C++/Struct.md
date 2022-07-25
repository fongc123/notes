# Struct
Contrary to arrays which store homogeneous objects, a <span style = "color:lightblue">structure</span> stores **heterogenous objects**.

## Definition & Syntax

Structures allow the creation of new user-defined data types using the keyword `struct`. Each object in a `struct` is referred to as a <span style = "color:lightblue">member</span> and can be any data type.

```C++
struct <STRUCT_NAME> {
	<DATA_TYPE> <MEMBER_NAME>;
	<DATA_TYPE> <MEMBER_NAME>;
	...
}
```

An <span style = "color:lightblue">instance</span> of a `struct` is created using the same syntax as instantiation of any other variable, allocating memory for the `struct`. Members are accessed using the dot notation.

```C++
int main() {
	<STRUCT_NAME> <STRUCT_VARIABLE_NAME>;

	<STRUCT_VARIABLE_NAME>.<MEMBER_NAME> = <VALUE>;
}
```

Structure variables can be initialized by **using curly braces**, **accessing members individually**, or **by using a function**.

### Example
A sample program that creates a user-defined data type called `Point`, which has two members, and showcases several methods of initializing its values.

```C++
struct Point {
	double x;
	double y;
};

void init_point(Point& p, float x, float y) {
	p.x = x; p.y = y;
}

int main() {
	Point point = { 49.2, 138.1 };
	point.x = 53.4; point.y = 122.9;
	init_point(point, 22.3, 58.1);

	return 0;
}
```
- note the `;` after the `struct` definition
- a `struct` needs to be **passed by reference** into the function to change it

## Array of Structures
An <span style = "color:lightblue">array of structures</span> is an array that consists of $N$ user-defined structures, where $N$ is the size of the array.

The below code block showcases this with an array that consists of dates.
```C++
struct Date {
	unsigned int year;
	unsigned int month;
	unsigned int day;
};

int main() {
	Date date[3] = {
		{2009, 10, 13},
		{2020, 1, 24},
		{2021, 5, 22}
	}
}
```

- since arrays are ordered, the structures can be *swapped* to arrange the dates in order

>[!INFO]
>The `sizeof()` function can be used to determine the size of an array.

## Linked Lists
A <span style = "color:lightblue">linked list</span> is a type of data structure that consists of a number of `struct` <span style = "color:lightblue">nodes</span> pointing to the next node using pointers (*see Pointers*).

```C++
struct Node {
	int data;
	Node* next;
};
```

They are <u>linked</u> in the sense that each instance of `Node` points to another instance of `Node` which is stored in the `next` member.

## Binary Tree
A <span style = "color:lightblue">binary tree</span> is another type of data structure, where the tree starts from a root node and each node has children nodes (*a left node and a right node*).

```C++
struct Node {
	int data;
	Node* left;
	Node* right;
}
```

> [!INFO]
> Look online for implementation on **linked lists** and **binary trees**.

