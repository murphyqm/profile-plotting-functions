#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/06/2021
by murphyqm

"""
x = [1140.1612128460838, 1166.9346282549693]
y = [60, 62]

m = (y[1] - y[0])/(x[1]- x[0])

# y = mx + c
# c = y - mx

c = y[0] - (m*x[0])
c2 = y[1] - (m*x[1])

# y =mx + c
# T = 0.07470096621801355(depth_in_km) -25.171144243904664
# depth = m*T + c
# (depth - c)/m = T


def Temp_from_depth(depth_in_km):
	T = (depth_in_km + 25.171144243904664)/0.07470096621801355
	return T

T = Temp_from_depth(61.0)
print(T)

T_difference = Temp_from_depth(60.9) - Temp_from_depth(61.1)
print(T_difference)
