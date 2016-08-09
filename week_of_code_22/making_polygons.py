# A polygon is a closed shape with three or more sides. For example,
# triangles are polygons. A polygon is non-degenerate if it has no overlapping
# sides (and no sides of zero length).
#
# You have  sticks with positive integer lengths, .A0, A1, .. An-1.
# You want to create a polygon using all  sticks. Because this is not always possible,
# you can cut one or more sticks into two smaller sticks
# (they do not necessarily need to be of integer length) and
# repeat the process of trying to create a polygon using all the sticks.
# Given the lengths of all n sticks, find and print the minimum number of
# cuts necessary to make a non-degenerate polygon.

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
if len(a) == 1:
    print(3)
elif len(a) == 2:
    print(1)
else:
    count = 0
    while True:
        a.sort()
        m = a.pop()
        if m >= sum(a):
            count += 1
            a.append(float(m/2))
            a.append(float(m/2))
        else:
            print(count)
            break
