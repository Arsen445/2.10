#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_mod(*args):
    
    if args:
        a = 0
        for arg in args:
            a = a + abs(arg)
        return a
    
    else:
        return None

if __name__ == "__main__":
    
    print(sum_mod(0, -5, 8.9, 4, 3, -9.5, 67, 3))
    print(sum_mod())
