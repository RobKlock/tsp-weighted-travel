''' Generate TSP art images with an optimal tour file '''

import random
import os
import shlex
from datetime import datetime

# Make the file
cur_date = datetime.now()
date_time = cur_date.strftime("%m-%d-%Y-%H-%M-%S")
fi = "tsp-{date}.eps"
filename = fi.format(date=date_time)
f = open(filename, "x")
# Dimension of grid, so the number of cities is DIMENSION ^ 2
DIMENSION = 40
TOURFILE = "tour.cyc"

# Dictionary of city coordinates
city_dictionary={}
city_num = 0
for x in range(1, DIMENSION + 1):
    for y in range(1, DIMENSION + 1):
        city_dictionary[city_num] = [x,y]
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
f.write(str(DIMENSION + 50)) 
f.write(" ") 
f.write(str(DIMENSION + 50)) 
f.write(""" \n""")
f.write("""%!        %special comment (file is PostScript) \n 0 0 moveto\nclosepath\n4 setlinewidth\nstroke\n0.5 0.5 scale\n""")
# For each city in our tour, find its coordinates
# and draw a dot and line to that location
f.write("\n%Draw Cities\n")
for x in range (1, DIMENSION + 1):
    for y in range (1, DIMENSION + 1):
        f.write(str(x * 50 + 20))
        f.write(" ")
        f.write(str(y * 50 + 20))
        f.write(" 4 0 360 arc\n")
        # if i == 4 and j == 2:
        #   f.write("""1 0 0 setrgbcolor\n""")
        #postScript_circle = "{x} {y} 4 0 360 arc"
        #draw_circle = "{x} {y} 4 0 360 arc".format(x=i * 5, y = j * 5)
        #f.write(postScript_circle.format(x=i * 5, y = j * 5))
        f.write("""\nfill\nstroke\n""")
        #if i == 4 and j == 2:
        #    f.write("""0 0 0 setrgbcolor\n""")
f.write("\n%Draw Tour\n")
f.write("\n2 setlinewidth\n70 70 moveto\n")
#f.write("20 20 moveto\n")
first_city = True
for i in map(lambda city: city_dictionary[int(city)], tour): 
    f.write(str(i[0] * 50 + 20))
    f.write(" ")
    f.write(str(i[1] * 50 + 20))
    f.write(" lineto\n")
    f.write("stroke\n")
    f.write(str(i[0] * 50 + 20))
    f.write(" ")
    f.write(str(i[1] * 50 + 20))
    f.write(" moveto\n")
f.write("""showpage\n""")
#os.system("open " + shlex.quote(filename))
