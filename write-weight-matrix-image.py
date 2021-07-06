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
    DL = 1
    DR = 1
    if p1 == p2:
        return 0
    X_MID = 110
    Y_MID = 110

    X_DIM = 220
    Y_DIM = 220
    """ if p1[0] % 10 == 0:
        if p2[1] == p1[1]:
            print("P1: ", p1)
            print("P2: ", p2) """

    if p1[2] == 127 and p2[2] == 127:
        V = 2
        H = .5
    if p1[2] == 0 and p2[2] == 0:
        V = .5
        H = 2
    """ if (p1[1] >= 4 and  p1[0] >= 4) and (p1[1] <= 16 and  p1[0] <= 16) and (p2[1] >= 4 and  p2 [0] >= 4) and p2[1] <= 16 and  p2[0] <= 16:
        H = .5
        V = 1
    elif (p1[1] >= 204 and  p1[0] >= 204) and (p1[1] <= 216 and  p1[0] <= 216) and (p2[1] >= 204 and  p2 [0] >= 204) and p2[1] <= 216 and  p2[0] <= 216:
        H = 1
        V = .5
 """
    '''
    # Quadrant 2
    # if p1[0] < X_MID/2 and p1[1] > Y_MID/2 and p2[0] < X_MID/2 and p2[1] > Y_MID/2:
    #     H = .5
    #     V = 1
    # # Quadrant 3
    # elif p1[0] < X_MID/2 and p1[1] < Y_MID/2 and p2[0] < X_MID/2 and p2[1] < Y_MID/2:
    #     H = 1
    #     V = .5
    # # Quadrant 1
    # elif p1[0] > X_MID/2 and p1[1] > Y_MID/2 and p2[0] > X_MID/2 and p2[1] > Y_MID/2:
    #     H = .5
    #     V = 1
    # # Quadrant 4
    # elif p1[0] > X_MID/2 and p1[1] < Y_MID/2 and p2[0] > X_MID/2 and p2[1] < Y_MID/2:
    #     H = 1
    #     V = .5

    # if p1[0] > 42 * 30 and p1[0] < 47 * 30 and p2[0] > 42 * 30 and p2[0] < 47 * 30 and p1[1] > 0 and p1[1] < 202 and p2[1] > 0 and p2[1] < 202 * 30:
    #     v = .5
    #     h = 1
    # elif p1[0] > 178 * 30 and p1[0] < 183 * 30 and p2[0] > 178 * 30 and p2[0] < 183 * 30 and p1[1] > 152 * 30 and p1[1] < 202 * 30 and p2[1] > 152 * 30 and p2[1] < 202 * 30:
    #     v = .5
    #     h = 1
    # elif p1[0] > 0 and p1[0] < 199 * 30 and p2[0] > 0 and p2[0] < 199 * 30 and p1[1] > 147 * 30 and p1[1] < 151 * 30 and p2[1] > 147 * 30 and p2[1] < 151 * 30:
    #     h = .5
    #     v = 1
    # elif p1[0] > 0 and p1[0] < 41 * 30 and p2[0] > 0 and p2[0] < 41 * 30 and p1[1] > 60 * 30 and p1[1] < 71 * 30 and p2[1] > 60 * 30 and p2[1] < 71 * 30:
    #     h = .5    
    #     v = 1 
    # Bottom main rectangle
    # if p1[0] > 0 and p1[0] < 4700 and p2[0] > 0 and p2[0] < 4700 and p1[1] > 0 and p1[1] < 4752 and p2[1] > 0 and p2[1] < 4752:
    #     V = .5
    #     H = 1
    # # Top right rectangle
    # if (p1[0] > 1316 and p1[0] < 4700) and (p2[0] > 1316 and p2[0] < 4700) and (p1[1] > 4752 and p1[1] < 6800) and (p2[1] > 4752 and p2[1] < 6800):
    #     V = 1
    #     H = .5
    # # 
    # elif p1[0] > 0 and p1[0] < 1316 and p2[0] > 0 and p2[0] < 1316 and p1[1] > 5469 and p1[1] < 6800 and p2[1] > 5469 and p2[1] < 6800:
    #     H = 1
    #     V = .5
    # elif p1[0] > 0 and p1[0] < 947 and p2[0] > 0 and p2[0] < 947 and p1[1] > 4752 and p1[1] < 5469 and p2[1] > 4752 and p2[1] < 5469:
    #     H = .5
    #     V = 1
    # # else:
    # #     h = .5  
    # #     v = 1  
'''
    return math.sqrt(((H * ((p1[0])-(p2[0]))) ** 2) + ((V*((DL * p1[1])-(DR * p2[1])))**2))
DOTSFILE = "dots.dat"
MASK_FILE = "test-mask.pgm"
# Read in our dots file
dots = open(DOTSFILE, "r")
dots_lines = dots.readlines()

mask_file = open(MASK_FILE, "r")
mask_lines = mask_file.readlines()
mask_rows = mask_lines[1].split(" ")[0]
mask_cols = mask_lines[1].split(" ")[1]
# Nested dictionary of PGM values
NUM_CITIES = int(dots_lines[0].split(" ")[0])

# Dictionary of city coordinates
city_dictionary={}
city_num = 0
for line_index in range(1, len(dots_lines)):
    
    city_dictionary[city_num] = [int(dots_lines[line_index].split(" ")[-2]), int(dots_lines[line_index].split(" ")[-1]), int(mask_lines[222 - int(dots_lines[line_index].split(' ')[-1]) * 220  + int(dots_lines[line_index].split(' ')[-2]) + 3].strip())]
    if (city_num == 113):
        print("city 113: ", int(dots_lines[line_index].split(' ')[-2]), " ,", int(dots_lines[line_index].split(' ')[-1]))
        print("city 113 PGM val: ", mask_lines[int(dots_lines[line_index].split(' ')[-2]) * 220 + int(dots_lines[line_index].split(' ')[-1]) - 3])
    city_num += 1
print("dict len ", len(city_dictionary))
# Print our largest x and y values
values = city_dictionary.values()

# Make the file
cur_date = datetime.now()
date_time = cur_date.strftime("%m-%d-%Y-%H-%M-%S")
fi = "weighted-grid-tsp-image-{date}.tsp"
filename = fi.format(date=date_time)
#print("Writing to file: ", filename, "\n")
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
EDGE_WEIGHT_FORMAT: UPPER_DIAG_ROW\n
EDGE_WEIGHT_SECTION\n""")
# For each city
for i in range(0,len(city_dictionary)):
    # Calculate the distance to every other city
    for j in range(i,len(city_dictionary)):
        distance = dist(city_dictionary[i], city_dictionary[j])
        f.write(str(int(distance)))
        f.write(" ")
    f.write("\n")
f.write("""
EOF
""")
print("\nRunning LINKERN...\n")
#os.system(COMMAND.format(file=filename))
#os.system("open " + shlex.quote(filename))


