''' Write TSP File with Weighted Edges '''

import random
import os
import shlex
from datetime import datetime
import math
DIMENSION = 10
# Weighted Distance Function
def dist(p1, p2):
    # Horizontal and vertical weights
    H = 1
    V = 1
    if p1 == p2:
        return 100
    return math.sqrt((H * ((p1[0] - p2[0])**2)) + (V * ((p2[0] + p2[1])**2)))
# Gather our cities
city_dictionary={}
city_num = 0
for i in range(1, DIMENSION + 1):
    for j in range(1, DIMENSION + 1):
        city_dictionary[city_num] = [i * 50 + 20,j * 50 + 20]
        city_num += 1
print(city_dictionary)
# Make the file
cur_date = datetime.now()
date_time = cur_date.strftime("%m-%d-%Y-%H-%M-%S")
fi = "weighted-grid-tsp-{date}.tsp"
filename = fi.format(date=date_time)
f = open(filename, "x")
DIMENSION = 10
f.write("""NAME: distance-matrix-tsp\n
TYPE: TSP\n
COMMENT: Test for distance matrix using Linkern algorithm (Klock and Cappelletti)\n
DIMENSION: 10\n
EDGE_WEIGHT_TYPE: EXPLICIT\n
EDGE_WEIGHT_FORMAT: FULL_MATRIX\n
EDGE_WEIGHT_SECTION\n""")
# For each city
for i in range(0,len(city_dictionary)):
    # Calculate the distance to every other city
    for j in range(0,len(city_dictionary)):
        distance = dist(city_dictionary[i], city_dictionary[j])
        f.write(str(int(distance)))
        f.write(" ")
    f.write("\n")
f.write("""
EOF
""")
#os.system("open " + shlex.quote(filename))