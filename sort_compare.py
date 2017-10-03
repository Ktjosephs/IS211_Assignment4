#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 sort_compare."""

import time
import random


def insertion_sort(a_list):
    """Insertion sort list."""
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    return end-start, a_list


def gap_insertion_sort(a_list, start, gap):
    """A gap sort function."""

    for x in range(start + gap, len(a_list), gap):
        current_value = a_list[x]
        position = x
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def shell_sort(a_list):
    """A shell list function."""
    start = time.time()
    list_count = len(a_list) // 2
    while list_count > 0:
        for start_position in range(list_count):
            gap_insertion_sort(a_list, start_position, list_count)
        list_count = list_count // 2
    end = time.time()
    return end-start, a_list


def python_sort(a_list):
    """A list sort function."""
    start = time.time()
    a_list = a_list.sort()
    end = time.time()
    return end-start, a_list


def random_list(average_time):
    """Generates a random list."""
    my_list = []
    for item in range(average_time):
        my_list.append(random.randint(1,average_time))
    return my_list


def main():
    """The main function of the program."""
    test_number = [500, 1000, 10000]

    for x in test_number:
        counter = 100
        result = [0, 0, 0]

        while counter > 0:
            my_list = random_list(x)
            result[0] += insertion_sort(my_list)[0]
            result[1] += shell_sort(my_list)[0]
            result[2] += python_sort(my_list)[0]
            counter -= 1
        print "For the list of {}... ".format(x)
        print "Insertion Sort took %10.7f seconds to run, on average." % (result[0] / 100)
        print "Shell Sort ' + 'took %10.7f seconds to run, on average." % (result[1] / 100)
        print "Python Sort ' + 'took %10.7f seconds to run, on average." % (result[2] / 100)

if __name__ == "__main__":
    main()
