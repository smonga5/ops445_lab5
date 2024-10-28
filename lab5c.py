#!/usr/bin/env python3
# Author ID: [smonga5]

def add(number1, number2):
    """Add two numbers together, return the result. If error, return 'error: could not add numbers'"""
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """Read a file and return a list of all lines. If error, return 'error: could not read file'"""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
        return 'error: could not read file'

# Main block to test the functions
if __name__ == '__main__':
    print(add(10, 5))                        # works, should print 15
    print(add('10', 5))                      # works, should print 15
    print(add('abc', 5))                     # exception, should print 'error: could not add numbers'
    print(read_file('seneca2.txt'))          # works, should print file contents
    print(read_file('file10000.txt'))        # exception, should print 'error: could not read file'
