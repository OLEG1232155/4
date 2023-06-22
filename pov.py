#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите два слова: ")
    s = s.replace(' ', '')
    k1 = 0

    for i in s:
        k = 0
        for j in s:
            if i == j:
                k += 1
        if k == 1:
            k1 = 1
            print(i)

    if k1 == 0:
        print("Все буквы в словах повторяются.")
