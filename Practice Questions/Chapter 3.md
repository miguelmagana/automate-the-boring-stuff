1. Why are functions advantageous to have in your programs?
   - Functions help from repeating code by allowing a block of code to be reused.
2. When does the code in a function execute: when the function is
defined or when the function is called?
   - The code in a function is executed when the function is called.
3. What statement creates a function?
   - The *def* statement defines a function.
4. What is the difference between a function and a function call?
   - A function is a reusable code block that can be called. A function call uses said function.
5. How many global scopes are there in a Python program? How many
local scopes?
   - There can only be one global scope. There can be many local scopes, for example within a function.
6. What happens to variables in a local scope when the function call returns?
   - The variables in a local scope get deleted after the function returns a value.
7. What is a return value? Can a return value be part of an expression?
   - A return value is returned after the code in a function is evaluated.
8. If a function does not have a return statement, what is the return value
of a call to that function?
   - A function that does not have a return value will return a None.
9. How can you force a variable in a function to refer to the global variable?
   - Using the *global* keyword in the function will refer to the global variable.
10. What is the data type of None?
    - None is of the None data type.
11. What does the import areallyourpetsnamederic statement do?
    - Imports the areallyyourpetsnamederic object to be used.
12. If you had a function named bacon() in a module named spam, how
would you call it after importing spam?
    - spam.bacon()
13. How can you prevent a program from crashing when it gets an error?
    - Use a try / catch block to catch the error and print it gracefully.
14. What goes in the try clause? What goes in the except clause?
    - The try clause has the block to be executed and catches the exception. The exeption handles what is done by the exception by printing the default exception from Python or printing out a custom exception set by the developer.