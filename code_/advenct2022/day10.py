from sys import stdin
import sys

stdin = open("input.txt", "r")
inputs = stdin.readlines()
X = 1
logs = []
for p in inputs:
    signal = p.split()
    if signal