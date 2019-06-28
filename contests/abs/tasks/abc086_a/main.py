#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def main():
    a, b = map(int,input().split(' '))
    if isEven(a) or isEven(b):
        print('Even')
    else:
        print('Odd')

def isEven(a):
    return a % 2 == 0

if __name__ == '__main__':
    main()

