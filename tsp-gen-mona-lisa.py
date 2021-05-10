''' Generate Mona Lisa TSP art image with dots.dat and tour files '''

import random
import os
import shlex
from datetime import datetime

# Make the file
cur_date = datetime.now()
date_time = cur_date.strftime("%m-%d-%Y-%H-%M-%S")
fi = "tsp-image-{date}.eps"
filename = fi.format(date=date_time)
print("Image is file ", filename)
f = open(filename, "x")
# Dimension of grid, so the number of cities is DIMENSION ^ 2
TOURFILE = "tour.cyc"
DOTSFILE = "dots.dat"
dots = open(DOTSFILE, "r")
dots_lines = dots.readlines()
#print(dots_lines)
#print(dots_lines[1].split(" "))
NUM_CITIES = int(dots_lines[0].split(" ")[0])
#print("NUM_CITIES: ", NUM_CITIES)
# Dictionary of city coordinates
city_dictionary={}
city_num = 0
for line_index in range(1, len(dots_lines)):
    city_dictionary[city_num] = [dots_lines[line_index].split(" ")[-2], dots_lines[line_index].split(" ")[-1]]
    city_num += 1
#print("city dictionary: \n", city_dictionary)

# Read tour file
opt_tour = open(TOURFILE, "r")
lines = opt_tour.readlines()
# Array for storing the path
tour = []
for line_index in range(1, len(lines)):
    tour.append(lines[line_index].split(" ")[0])

    # Add our first city to the end of the tour
    if line_index == len(lines) -1:
        tour.append(lines[1].split(" ")[0])

# Map over our tour and grab the corresponding coordinates
coordinates = map(lambda city: city_dictionary[int(city)], tour)
tour_coordinates = list(coordinates)
# print("tour coordinates: \n", tour_coordinates)
# print(tour_coordinates)
# print("tour:\n", tour)
f.write("""%%BoundingBox: 0 0 """)
f.write(str(4700)) 
f.write(" ") 
f.write(str(6800)) 
f.write(""" \n""")
f.write("""%!        %special comment (file is PostScript) \n 0 0 moveto\nclosepath\n4 setlinewidth\nstroke\n0.1 0.1 scale\n""")
# For each city in our tour, find its coordinates
# and draw a dot and line to that location
f.write("\n%Draw Cities\n")
for i in range (0, NUM_CITIES): 
    f.write(str(city_dictionary[i][0]))
    f.write(" ")
    f.write(str(city_dictionary[i][1]))
    f.write(" 4 0 360 arc\n")
    f.write("""\nfill\nstroke\n""")

f.write("\n%Draw Tour\n")
f.write("\n2 setlinewidth\n")
f.write(str(city_dictionary[int(tour[0])][0]))
f.write(" ")
f.write(str(city_dictionary[int(tour[0])][1]))
f.write(" moveto\n")
first_city = True
for i in map(lambda city: city_dictionary[int(city)], tour): 
    f.write(str(int(i[0])))
    f.write(" ")
    f.write(str(int(i[1])))
    f.write(" lineto\n")
    f.write("stroke\n")
    f.write(str((int(i[0]))))
    f.write(" ")
    f.write(str((int(i[1]))))
    f.write(" moveto\n")
f.write("""showpage\n""")
#os.system("open " + shlex.quote(filename))