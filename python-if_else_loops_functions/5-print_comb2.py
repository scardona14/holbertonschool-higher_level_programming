#!/usr/bin/python3
for number in range(0, 100):
    if number < 100:
        print('{:02d}'.format(number), end=", ")
    else:
        print("{}".formar(number))

