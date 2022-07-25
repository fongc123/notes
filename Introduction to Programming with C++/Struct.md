# Struct
Contrary to arrays which store homogeneous objects, a <span style = "color:lightblue">structure</span> stores **heterogenous objects**.

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
int main()
```