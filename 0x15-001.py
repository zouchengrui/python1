#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#根据输入出生年份判断00前和00后
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
