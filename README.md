# DistanceVectorRouting
201501087.py is a program that takes an input file and then runs the bellaman ford
algorithm and finally output the shortest cost from each node to every other node.
For eg: 
Input file: 
5
2 2 2 4 5
4 1 2 3 14 4 5 5 4
2 2 14 5 34
3 1 5 2 5 5 58
3 2 4 3 34 4 58
(refer to image 'cn.png' for the given graph)

Output:
5
4 2 2 3 16 4 5 5 6 (shortest distance of 1: from 2 = 2units, from 3 = 16units, from 4 = 5units, from 5 = 6units for the given graph)
4 1 2 3 14 4 5 5 4
4 1 16 2 14 4 19 5 18
4 1 5 2 5 3 19 5 9
4 1 6 2 4 3 18 4 9

