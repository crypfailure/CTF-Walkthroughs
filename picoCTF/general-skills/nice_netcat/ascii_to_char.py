#!/usr/bin/python3

f = open("output", "r")

for char in f:
    print(chr(int(char)), end = "")
