#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def n_run(**birds):
    for bird,name in birds.items():
        print(f"{bird}: {name}")



if __name__ == "__main__":
    n_run(виды_ночных_поедателей_мышей =["сова", "филин", "owl"],
          виды_жертв = ["заяц", "крыса", "мышь"])
