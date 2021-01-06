def spam(divide_by):
    # Exception handling
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
