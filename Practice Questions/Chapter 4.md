1. What is []?
   - The square brackets represent a list.
2. How would you assign the value 'hello' as the third value in a list stored
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
   - spam[2] = 'hello'
- *For the following three questions, let’s say spam contains the list ['a',
'b', 'c', 'd'].*
3. What does spam[int(int('3' * 2) / 11)] evaluate to?
   - This throws an error because of the different data types
4. What does spam[-1] evaluate to?
   - 'd'
5. What does spam[:2] evaluate to?
    - 'a' and 'b'
- *For the following three questions, let’s say bacon contains the list
[3.14, 'cat', 11, 'cat', True].*
  
6. What does bacon.index('cat') evaluate to?
   - Index of 1
7. What does bacon.append(99) make the list value in bacon look like?
   - Adds 99 to the end of the list
8. What does bacon.remove('cat') make the list value in bacon look like?
   - Removes 'cat' from the list
9. What are the operators for list concatenation and list replication?
   - The + and += works with lists and strings
10. What is the difference between the append() and insert() list methods?
   - The append() method adds the item to the end of the list while the insert() method will put an item anywhere in the list given the right parameters
     
11. What are two ways to remove values from a list?
    - The *del* statement when you know the index and the remove() method when you do not know the index.
12. Name a few ways that list values are similar to string values.
    - List values can be concatenated and sliced like strings.
13. What is the difference between lists and tuples?
    - Lists are mutable (you can mutate them) while tuples are immutable and the values can only be referenced not changed
14. How do you type the tuple value that has just the integer value 42 in it?
    - the_tuple(42,) the comma signifies it's a tuple and not a list
15. How can you get the tuple form of a list value? How can you get the list
form of a tuple value?
    
16. Variables that “contain” list values don’t actually contain lists directly.
What do they contain instead?
    - using the list() and tuple() methods to swap between both types
17. What is the difference between copy.copy() and copy.deepcopy()?
    - copy.copy() will copy one item while copy.deepcopy() will copy a list recursively