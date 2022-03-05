# Write a function that takes a list value as an argument
# Returns a string with all the items separated by comma and a space, with 'and' inserted before the last item

spam = ['apples', 'bananas', 'grapes', 'frogs']

def separatorFunction(spam): # The function taking a list
    for i in range(len(spam)): # The loop to iterate through the list
        print(str(i[0]) + ', ' + str(i[1]) + ', ' + str(i[2]) + ', and ' + str(i[3]))

separatorFunction(spam)