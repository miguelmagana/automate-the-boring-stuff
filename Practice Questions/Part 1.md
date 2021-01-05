# How to Automate the Boring Stuff
## Part 1 - Python Basics

## End of Chapter Practice

1. Which of the following are operators and which are values?

- \* = multiplication operator
- \'hello' = literal value
- \-88.8 = float value
- \- = minus operator
- \/ = division operator
- \+ = addition operator
- 5 = integer value

2. Which of the following is a variable and which is a string?

- spam = the variable called spam
- 'spam' = the spam string literal

3. Name three data types?

- int (a whole number, 1)
- float (a floating point number, 3.14)
- string (a string of characters, 'One2ThreeFour', may include numbers, '1')

4. What is an expression made up of? What do all expressions do?

- Expressions consist of values and operators, and they can always evaluate down
to a single value (2 + 2 = 4)

5. This chapter introduced assignment statements, like spam = 10 . What is
the difference between an expression and a statement?

- An *expression* will evaluate to value, a *statement* does something

6. What does the variable bacon contain after the following code runs?
    ```python
    bacon = 20
    bacon + 1
    ```
   - bacon = 21
    
7. What should the following two expressions evaluate to?
    ```python
    'spam' + 'spamspam'
    'spam' * 3
    ```
    - both evaluate to 'spamspamspam'
    
8. Why is eggs a valid variable name while 100 is invalid?
- Variables can only be one word
- It can use only letters, numbers, and the underscore ( _ ) character
- It can’t begin with a number

9. What three functions can be used to get the integer, floating-point
number, or string version of a value?
   - int()
   - float()
   - str()
    
10. Why does this expression cause an error? How can you fix it?
```python
'I have eaten ' + 99 + ' burritos'
```
- The 99 is the value of 99. The value needs to be converted to a string using the str().

Extra Credit:
- Search online for the Python documentation for the len()
function
  > Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).