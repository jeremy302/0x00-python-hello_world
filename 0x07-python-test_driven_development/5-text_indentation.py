#!/usr/bin/python3
'''This modules contains a function to indent text with some symbols

Example:
text_indentation('ab.c') -> "ab.\n\nc"
'''


def text_indentation(text):
    ''' indents and prints a text

    a newline is printed after a '.', ':', or '?'.
    whitespaces are trimmed at the start and end of lines

    Args:
        text (str): text to print
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip(' ')
    tlen = len(text)
    txt = ''
    buf = ''
    i = 0
    while i < tlen:
        c = text[i]
        if c == '\n':
            txt += buf.strip() + c
            buf = ''
        elif c in '.:?':
            txt += (buf + c).strip() + '\n\n'
            buf = ''
        else:
            buf += c
        i += 1
    txt += buf.strip()
    print(txt, end='')
