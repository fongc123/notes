# Classes
A <span style = "color:lightblue">class</span> allows different pieces of information to be grouped under a single object.

The C++ class is a generalization of `struct`. In addition to storing **heterogeneous objects**, C++ classes support **a set of operations** and **access control** to those objects.
- <span style = "color:lightblue">data members</span>: data (*similar to* `struct`)
- <span style = "color:lightblue">member functions</span>: functions that only work for the objects in a class
- <span style = "color:lightblue">access control</span>: scope in which the class objects can be accessed
	- <span style = "color:lightblue">public</span>: accessible to all (both member functions *and* non-member functions)
	- <span style = "color:lightblue">private</span>: accessible to only member functions
	- <span style = "color:lightblue">protected</span>: ==???==
- <span style = "color:lightblue">object-oriented programming (OOP)</span>: divide tasks into smaller tasks to accomplish a goal

Classes allow code to be organized more effectively, showing only the **necessary** parts for use outside the class (*public functions*) and **prohibiting** direct modification of data members.

## Syntax
The below code block shows the syntax for creating a class.
```C++
class Example {
	private:
		int data1;
		int data2;

	public:
		// constructor
		Example();

		// accessors
		int fun1() const;
		int fun2() const;
		int fun3() const;

		// mutator
		void set(int, int);

		// destructor
		~Example();
}
```

> [!INFO]
> Accessor functions have `const` in their function definition or function declaration, as these functions shouldn't be able to modify the data members.

## Constructors & Destructors
<span style = "color:lightblue">Constructors</span> and <span style = "color:lightblue">destructors</span> are functions that are used to **create** and **delete** the class object respectively. The constructor is *always* called when the object is instantiated and often initializes the object's contents.

A class can have more than one constructor but one and only one destructor.

An object is constructed when **it is defined in a scope (*stack*)** or when **it is created with the `new` operator (*heap*)**. An object is destructed when **it goes out of scope (*stack*)** or when **it is deleted with the `delete` operator (*heap)***.

> [!INFO]
> The **heap** is a free-floating region of the memory which is not managed by the CPU (i.e., it may not be deallocated when the program exits the relevant scope). Instead, the programmer has to manage it themselves.

## Default Constructors & Destructors
C++ will automatically generate the default constructor or destructor when not provided.

The <span style = "color:lightblue">default constructor</span> allocates enough memory but does not initialize the content of its data members. The <span style = "color:lightblue">default destructor</span> simply releases memory.

**Default constructors and destructors are inadequate for dynamic data memebers (i.e., heap).**
