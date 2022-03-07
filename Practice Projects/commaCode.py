# Write a function that takes a list value as an argument
# Returns a string with all the items separated by comma and a space, with 'and' inserted before the last item
# Used stackoverflow for help

from ntpath import join


def list_thing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']

print(list_thing(spam))