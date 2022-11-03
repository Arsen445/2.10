#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sred_geom(*args):
    
    if args:
        a = 0
        k = 0
        for arg in args:
            a = a + (1 / arg)
            k = k + 1  
        h = k / a
        return h
    
    else:
        return None

if __name__ == "__main__":
    
    print(sred_geom(1, 5, 8.9, 4, 3, 9.5, 67, 3))
    print(sred_geom())
