#!/usr/bin/env python

# import the modules used in this file
import sys
import binky

# Defines a repeat function that takes 2 arguments
def repeat(s, exclaim):
    """
    Returns the string s repeat 3 times
    If exclam is true, append exclamation marks.
    """
    result = s + s + s # Can also use s * 3 which is faster (Whay?)
    if exclaim:
        result = result + '!!!'

    return result

# Gather our code in a main() function
def main():
    print 'Hello There ', sys.argv[1]
    print len(sys.argv)
    print repeat('Yay', False)
    print repeat('Whoa', True)
    print binky.foo()

if __name__ == '__main__':
    main()
