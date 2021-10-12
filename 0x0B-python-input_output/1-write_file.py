#!/usr/bin/python3
'''
Defines a function number_of_lines
'''


def write_file(filename="", text=""):
    '''a function that writes a string to a text file
    (UTF8) and returns the number of characters written
    ARGS:
        filename: (str) name of file or path to write to
        text: (str) text to write to file
    Return:
        number of text
    '''
    with open(filename, mode='w', encoding='utf8') as f:
        f.write(text)
    return len(text)
