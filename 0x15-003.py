#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#计算BMI指数
height=input('height:')
weight=input('weight:')
BMI=float(weight)/(float(height)*float(height))
print('BMI:',BMI)
if BMI<18.5:
    print('过轻')
elif 18.5<=BMI<25:
    print('正常')
elif 25<=BMI<28:
    print('过重')
elif 28<=BMI<32:
    print('肥胖')
else:
    print('严重肥胖')
