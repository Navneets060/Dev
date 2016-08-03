#!/bin/bash

awk '/test/ {print}' /c/cygwin64/dummy.txt

echo No. of times 'test' appeared in the given scenario is : 

awk '/test/ {i=i+1} END {print i}' /c/cygwin64/dummy.txt

wc --words --lines --bytes /c/cygwin64/dummy.txt

sort /c/cygwin64/dummy.txt
