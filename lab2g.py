#!/usr/bin/env python3

## Author: Mohd Abrar Hossain
## Author ID: mhossain69@myseneca.ca
## Date Created: 2024/05/15

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')