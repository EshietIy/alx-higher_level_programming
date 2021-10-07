#!/usr/bin/python3
'''A Text Indentation module
a function that prints a text
with 2 new lines after each of these character: '.,?'
'''


def text_indentation(text):
    '''
    A function that prints a text
    with 2 new lines after each of these characters: .,? and :

    Args:
    text: (str)

    Raise:
        TypeError

    Return:
        None
    '''
    new_str = ''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == " " and len(new_str) == 0:
            continue
        if i in '.?:':
            new_str += i
            print(new_str)
            print()
            new_str = ''
        else:
            new_str += i
    print(new_str, end='')
