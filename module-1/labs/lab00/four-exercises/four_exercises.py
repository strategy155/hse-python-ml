#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def divisible(begin, end):
    """
    :param begin: positive integer
    :param end: positive integer
    :return: str, string of space separated integers

    Examples of usage:
    >>> divisible(1, 10)
    '7'
    >>> divisible(1, 17)
    '7 14'
    >>> len(divisible(100, 1000))
    407
    >>> divisible(29, 60)
    '42 49 56'
    >>> len(divisible(300, 3000).split())
    309
    >>> ns = [int(n) for n in divisible(300, 10000).split()]
    >>> seven_mask = [not bool(n % 7) for n in ns]
    >>> all(seven_mask)
    True
    >>> any(seven_mask)
    True
    >>> five_mask = [not bool(n % 5) for n in ns]
    >>> all(five_mask)
    False
    >>> any(five_mask)
    False
    >>> divisible(2, 5)
    ''
    >>> 1329 not in ns
    True
    """
    raise NotImplementedError


def register_count(string):
    """

    :param string:
    :return: dict

    >>> register_count("Mama")
    {'UPPER': 1, 'LOWER': 3}
    >>> register_count("Your Name")
    {'UPPER': 2, 'LOWER': 6}
    >>> register_count("LingvoX!!!")
    {'UPPER': 2, 'LOWER': 5}
    >>> register_count("Труд, мир, май! Жвачка!")
    {'UPPER': 2, 'LOWER': 14}
    >>> register_count("Цой ЖИВ!,,,,,")
    {'UPPER': 4, 'LOWER': 2}
    """
    raise NotImplementedError


def pairwise_diff(left, right):
    """

    :param left: str
    :param right: str
    :return: float, percentage of different letters

    >>> pairwise_diff('ABSD', 'ABCD')
    0.25
    >>> pairwise_diff('aBSD', 'ABCD')
    0.5
    >>> pairwise_diff('LingvX', 'SpaceX')
    0.83
    >>> pairwise_diff('LingvoX', 'SpaceX')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pairwise_diff('abc', 'ab')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> left = 'Salaman..'; right = 'Salaman.!'
    >>> round(1. / len(left), 2) == pairwise_diff(left, right)
    True
    >>> pairwise_diff(left + right, left + left)
    0.06
    >>> pairwise_diff(left * 3, right * 2 + left)
    0.07
    """
    raise NotImplementedError


def run_robot():
    """

    :return:
    """
    NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
