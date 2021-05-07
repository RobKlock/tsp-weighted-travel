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
DIMENSION = 10
TOURFILE = "test-tour.cyc"

# Dictionary of city coordinates
cities = open('lin105.tsp', 'r')
cities_lines = cities.readlines()
city_dictionary={}
city_num = 0
for i in range(1, DIMENSION + 1):
    for j in range(1, DIMENSION + 1):
        city_dictionary[city_num] = [i,j]
        # print(city_num)
        city_num += 1

# Read tour file
opt_tour = open(TOURFILE, "r")
lines = opt_tour.readlines()
# Array for storing the path
tour = []
for line_index in range(1, len(lines)):
    tour.append(lines[line_index].split(" ")[0])
print(tour)
'''
cities = {

for line_index in range(6, len(cities_lines)):
    city_index = ''
    city_x = ''
    city_y = ''
    for i in cities_lines[line_index]:
'''    
# print(tour)
f.write("""%%BoundingBox: 0 0 200 200
%!        %special comment (file is PostScript) \n0 0 moveto\nclosepath\n4 setlinewidth\nstroke\n""")
# For each city in our tour, find its coordinates
# and draw a dot and line to that location
f.write("\n%Draw Cities\n")
for i in range (0, DIMENSION):
    for j in range (0, DIMENSION):
        f.write(str(i * 50 + 20))
        f.write(" ")
        f.write(str(j * 50 + 20))
        f.write(" 4 0 360 arc\n")
        #postScript_circle = "{x} {y} 4 0 360 arc"
        #draw_circle = "{x} {y} 4 0 360 arc".format(x=i * 5, y = j * 5)
        #f.write(postScript_circle.format(x=i * 5, y = j * 5))
        f.write("""\nfill\nstroke\n""")

f.write("""showpage\n""")
#os.system("open " + shlex.quote(filename))