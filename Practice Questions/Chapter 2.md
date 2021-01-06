# How to Automate the Boring Stuff
## Part 2 - Flow Control

## End of Chapter Practice

1. What are the two values of the Boolean data type? How do you
write them?
   - True
   - False
2. What are the three Boolean operators?
   - and
   - or
3. Write out the truth tables of each Boolean operator (that is, every
possible combination of Boolean values for the operator and what
they evaluate to).
 
   - 'True and True = True'
   - 'True and False = False'
   - 'False and True = False'
   - 'False and False = False'
   
   - True or True = True
   - True or False = True
   - False or True = True
   - False or False = False

4. What do the following expressions evaluate to?
```python
(5 > 4) and (3 == 5) 
= False
not (5 > 4) 
= False
(5 > 4) or (3 == 5) 
= True
not ((5 > 4) or (3 == 5)) 
= False
(True and True) and (True == False) 
= False
(not False) or (not True) 
= True
```
5. What are the six comparison operators?
   - == equal to
   - != not equal to
   - < less than
   - "> greater than"
   - ">= greater than or equal to"
   - <= less than or equal to
6. What is the difference between the equal to operator and the assignment operator?
   - The equal to operator asks whether the two values are the same
   - The equal assigns the value on the right to the variable on the left
7. Explain what a condition is and where you would use one.
   - A condition is tested for loops. If the condition is true then the block of code will run.
8. Identify the three blocks in this code:
```python
# Indent the blocks under the loops
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
```

9. Write code that prints Hello if 1 is stored in spam , prints Howdy if 2 is
stored in spam , and prints Greetings! if anything else is stored in spam .
```python
spam = 0
if spam == 1:
   print("Hello")
elif spam == 2:
   print("Howdy")
else:
   print("Greetings!")
```
10. What can you press if your program is stuck in an infinite loop?
    - Ctrl + C will send a KeyboardInterrupt to the program to stop it.
11. What is the difference between break and continue ?
    - The break will exit the program without running the rest of the code. The contiue will evaluate the code and will continue whether the condition is False or not.
12. What is the difference between range(10) , range(0, 10) , and range(0, 10, 1) in a for loop?
- range(10) - gives you a range from 0-9
- range(0,10) - gives you a range from 0-9, not including 10
- range(0, 10, 1) - gives you a range from 0-9, steps by 1

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using
a while loop.
    
```python
for number in range(10):
    print(number)

# Set the number to 0
number = 0
# Test the condition
while number <= 10:
    print(number)
    # Iterate the number to move through the range
    number += 1
```
14. If you had a function named bacon() inside a module named spam , how
would you call it after importing spam ?
    - You would call the bacon() method by creating a variable that is equal to the spam object of bacon().
    - 'spam.bacon()'
15. Extra credit: Look up the round() and abs() functions on the Internet,
and find out what they do. Experiment with them in the interactive shell.
    - round() rounds the value, parameters to round up or down can be used
    - abs() gives you the absolute value