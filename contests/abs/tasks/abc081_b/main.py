#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def main():
    n = input()
    l = map(map(int, input().split(' '))
    cnt = 0
    for i in l:
        if i == '1':
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()

