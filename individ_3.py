#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    t = -1
    s1 = ''

    for i in range(0, len(s), 2):
        if i > len(s):
            break
        if s[i] == 'о':
            s1 += s[t + 1:i]
            t = i

    s1 += s[t + 1:]

    print("Отредактированное предложение: ", s1)
