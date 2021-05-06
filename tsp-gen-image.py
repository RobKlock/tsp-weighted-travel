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
opt_tour = open('lin105.opt.tour', 'r')
lines = opt_tour.readlines()
tour = []
DIMENSION = 10
# Array for storing the path
for line_index in range(4, len(lines)):
    for i in lines[line_index]:
        if i.isdigit() == True:
            tour.append(lines[line_index].rstrip())

# Dictionary of city coordinates
cities = open('lin105.tsp', 'r')
cities_lines = cities.readlines()
'''
cities = {

for line_index in range(6, len(cities_lines)):
    city_index = ''
    city_x = ''
    city_y = ''
    for i in cities_lines[line_index]:
'''    
# print(tour)
f.write("""%!        %special comment (file is PostScript) \n0 0 moveto\nclosepath\n4 setlinewidth\nstroke\n""")
# For each city in our tour, find its coordinates
# and draw a dot and line to that location
f.write("\n%Draw Cities\n")
for i in range (0, DIMENSION):
    for j in range (0, DIMENSION):
        f.write(str(i * 50))
        f.write(" ")
        f.write(str(j * 50))
        f.write(" 4 0 360 arc\n")
        #postScript_circle = "{x} {y} 4 0 360 arc"
        #draw_circle = "{x} {y} 4 0 360 arc".format(x=i * 5, y = j * 5)
        #f.write(postScript_circle.format(x=i * 5, y = j * 5))
        f.write("""\nfill\nstroke\n""")

f.write("""showpage\n""")
#os.system("open " + shlex.quote(filename))