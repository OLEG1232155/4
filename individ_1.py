#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    a = input("Введите символ: ")

    k = s.count(a)

    if k == 0:
        print("В предложении нет данного символа.")
    else:
        i = 1
        while i <= k:
            print(a)
            i += 1
