#!/usr/bin/python3
def print_last_digit(number):
    num = number % 10
    print("{:d}".format(num), end="")
    return num