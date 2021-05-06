''' Write TSP File with Weighted Edges '''

import random
import os
import shlex
from datetime import datetime
# Make the file
cur_date = datetime.now()
date_time = cur_date.strftime("%m-%d-%Y-%H-%M-%S")
fi = "weighted-grid-tsp-{date}.tsp"
filename = fi.format(date=date_time)
f = open(filename, "x")
DIMENSION = 100
f.write("""NAME: distance-matrix-tsp\n
TYPE: TSP\n
COMMENT: Test for distance matrix using Linkern algorithm (Klock and Cappelletti)\n
DIMENSION: 100\n
EDGE_WEIGHT_TYPE: EXPLICIT\n
EDGE_WEIGHT_FORMAT: UPPER_ROW\n
EDGE_WEIGHT_SECTION\n""")
for i in range (1, DIMENSION):
    for j in range (0, DIMENSION - i):
        if i < DIMENSION / 2:
            f.write("1 ")
        else:
            f.write("2 ")
    f.write("\n")
f.write("""
EOF
""")
#os.system("open " + shlex.quote(filename))