#!/usr/bin/env python3
import sys, time

if len(sys.argv) != 2:
    print("Usage: main.py <problem_number>")
    sys.exit(1)

n = sys.argv[1].zfill(3)
mod = __import__(f"src.{n}", fromlist=["solve"])

t0 = time.time()
ans = mod.solve()
t1 = time.time()

print(f"Answer: {ans}")
print(f"Solved in {t1 - t0:.6f} seconds")
