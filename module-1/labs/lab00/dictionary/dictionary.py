#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def reverse_dictionary(dictionary):
    """
    Function reverses dictionary with structure { key: [values] } to
    dictionary with structure {value: [keys]}.

    >>> res = reverse_dictionary( {1: [4], 2: [3]} )
    >>> true_res1 = {3: [2], 4: [1]}
    >>> true_res1 == res
    True

    >>> res = reverse_dictionary( {1: [3, 4, 5]} )
    >>> true_res2 = {3: [1], 4: [1], 5: [1]}
    >>> true_res2 == res
    True

    >>> res = reverse_dictionary( {'hello': ['привет', 'здравствуй'], 'python': ['питон'] })
    >>> true_res3 = {'здравствуй': ['hello'], 'привет': ['hello'], 'питон': ['python']}
    >>> true_res3 == res
    True

    """
    raise NotImplementedError


def parse_dictionary(text):
    """
    Function forms dictionary from input text.

    >>> parse_dictionary('мама - mommy')
    {'мама': ['mommy']}
    >>> parse_dictionary('hello - привет, здравствуй')
    {'hello': ['привет', 'здравствуй']}
    >>> parse_dictionary('hello - привет, здравствуй, здорова')
    {'hello': ['привет', 'здравствуй', 'здорова']}
    >>> parse_dictionary("мама - mommy, mom\\nпапа - daddy, father")
    {'мама': ['mommy', 'mom'], 'папа': ['daddy', 'father']}
    >>> parse_dictionary("сын - son\\nпапа - daddy, father")
    {'сын': ['son'], 'папа': ['daddy', 'father']}
    """
    raise NotImplementedError


def print_dictionary(dictionary):
    with open('output.txt', 'w') as out:
        for key in sorted(dictionary):
            print(key + ' - ' + ', '.join(dictionary[key]), file=out)


def main():
    text = sys.stdin.read()
    base_dictionary = parse_dictionary(text)
    reversed_dictionary = reverse_dictionary(base_dictionary)
    print_dictionary(reversed_dictionary)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
