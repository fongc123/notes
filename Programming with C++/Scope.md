# Scope
<span style = "color:lightblue">Scope</span> is the region of code in which an <span style = "color:lightblue">identifier declaration</span> (i.e., a variable) is active. An identifier is only active until the end of its scope.

There exists two kinds of scopes: <span style = "color:lightblue">global</span> and <span style = "color:lightblue">local</span>.

## File Scope
File scope is the technical term for global scope. All functions can access <span style = "color:lightblue">global variables</span> (i.e., variables with global scope).

>[!INFO]
>If declared but uninitialized, global variables are initialized to zero instead of garbage.

## Local Scopes
### Function Scope
Function scope refers to the scope within a function. All variables declared with function scope only **exist** when the function is called and are **destructed** when the function ends.

## Block Scope
Block scope refers to the scope within a block (i.e., within `{` and `}`).

## Additional Notes
Listed below are useful notes that should be considered.
- identifiers with the **same name** cannot be used in the **same scope**, but they can be used in different scopes
- the compiler will choose the variable in the **innermost scope**
- global variables are not recommended → **use functions to pass variables** and **use local variables** instead

