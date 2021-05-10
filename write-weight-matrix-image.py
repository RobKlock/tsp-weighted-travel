''' Write TSP File with Weighted Edges from an image (.dat file)'''

import random
import os
import shlex
from datetime import datetime
import math

# Weighted Distance Function
def dist(p1, p2):
    # Horizontal and vertical weights
    H = 1
    V = 1
    if p1 == p2:
        return 0
    MID = 3000
    # # Quadrant 2
    # if p1[0] < MID/2 and p1[1] > MID/2 and p2[0] < MID/2 and p2[1] > MID/2:
    #     H = 1
    #     V = 1
    # # Quadrant 3
    # elif p1[0] < MID/2 and p1[1] < MID/2 and p2[0] < MID/2 and p2[1] < MID/2:
    #     H = 1
    #     V = 1
    # # Quadrant 1
    # elif p1[0] > MID/2 and p1[1] > MID/2 and p2[0] > MID/2 and p2[1] > MID/2:
    #     H = 1
    #     V = 1
    # # Quadrant 4
    # elif p1[0] > MID/2 and p1[1] < MID/2 and p2[0] > MID/2 and p2[1] < MID/2:
    #     H = 1
    #     V = 1

    if p1[0] > 42 and p1[0] < 47 and p2[0] > 42 and p2[0] < 47 and p1[1] > 0 and p1[1] < 202 and p2[1] > 0 and p2[1] < 202:
        v = .5
    elif p1[0] > 178 and p1[0] < 183 and p2[0] > 178 and p2[0] < 183 and p1[1] > 152 and p1[1] < 202 and p2[1] > 152 and p2[1] < 202:
        v = .5
    elif p1[0] > 0 and p1[0] < 199 and p2[0] > 0 and p2[0] < 199 and p1[1] > 147 and p1[1] < 151 and p2[1] > 147 and p2[1] < 151:
        h = .5
    elif p1[0] > 0 and p1[0] < 41 and p2[0] > 0 and p2[0] < 41 and p1[1] > 60 and p1[1] < 71 and p2[1] > 60 and p2[1] < 71:
        h = .5    
    elif p1[0] > 185 and p1[0] < 198 and p2[0] > 185 and p2[0] < 198 and p1[1] > 173 and p1[1] < 180 and p2[1] > 173 and p2[1] < 180:
        h = .5        

    return math.sqrt(((H * (p1[0]-p2[0])) ** 2) + ((V*(p1[1]-p2[1]))**2))
DOTSFILE = "dots.dat"
# Read in our dots file
dots = open(DOTSFILE, "r")
dots_lines = dots.readlines()
NUM_CITIES = int(dots_lines[0].split(" ")[0])

# Dictionary of city coordinates
city_dictionary={}
city_num = 0
for line_index in range(1, len(dots_lines)):
    city_dictionary[city_num] = [int(dots_lines[line_index].split(" ")[-2]), int(dots_lines[line_index].split(" ")[-1])]
    city_num += 1
print("dict len ", len(city_dictionary))
# Print our largest x and y values
values = city_dictionary.values()

# Make the file
cur_date = datetime.now()
date_time = cur_date.strftime("%m-%d-%Y-%H-%M-%S")
fi = "weighted-grid-tsp-image-{date}.tsp"
filename = fi.format(date=date_time)
print("Writing to file: ", filename, "\n")
print("Copy the following command to run LINKERN\n")
COMMAND = "./linkern -o tour.cyc {file}"
print(COMMAND.format(file=filename))
f = open(filename, "x")

f.write("""NAME: distance-matrix-tsp from image\n
TYPE: TSP\n
COMMENT: Test for distance matrix using Linkern algorithm (Klock and Cappelletti)\n
DIMENSION: """)
f.write(str(NUM_CITIES)) 
f.write("""\n
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
