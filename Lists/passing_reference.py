def eggs(some_parameter):
    some_parameter.append('Hello')


# Even though spam and some_parameter contain separate references, they
# both refer to the same list.
spam = [1, 2, 3]
eggs(spam)
print(spam)
