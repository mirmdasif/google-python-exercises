#!/usr/bin/env python

import sys

def main():
    s = 'hi'
    print s[1]
    print len(s)
    print s + ' there'

    pi = 3.14
    text = 'The value of pi is ' + str(pi)
    print text
    print r'this\t\n and that'
    print 'this\t\n and that'
    multi = """It was the best of times
    It was the worst of times."""
    print multi

    # String methods
    print "CAPS".lower();

    # String Slices
    s = 'Hello'
    print 'Hello s[1] =' + s[1]
    print 'Hello s[0] =' + s[-0]
    print 'Hello s[-5] =' + s[-5]
    print 'Hello s[-1:] =' + s[-1:]
    print 'Hello s[0:-1] =' + s[0:-1]
    print 'Hello s[:1] + s[1:] = ' + s[:1] + s[1:]

    # % Operator
    print ('%d little pigs come out, or I will %s, %s, and %s' %
        (3, 'huff', 'puff', 'blow down'))

    # i18n Strings (Unicode)
    ustring = u'A unicode \u018e string \xf1'
    print ustring
    s = ustring.encode('utf-8')
    print s
    print unicode(ustring.encode('utf-8'), 'utf-8')

if __name__ == '__main__':
    main()
