#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_scores(student, *scores):
    print(f"student Name: {student}")
    for score in scores:
        print(score)

if __name__ == '__main__':
    i = [100, 123, 35, 46, 46]
    print_scores("DK", *i)
