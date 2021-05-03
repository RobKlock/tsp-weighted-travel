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
# Array for storing the path
for line in lines:
    for i in line:
        if i.isdigit() == True:
            tour.append(line)

print(tour)

f.write("""
    %!PS-Adobe-3.0 EPSF-3.0 \n
    %%BoundingBox: 0 0 400 400 \n

    0.7 setgray \n

    1 setlinejoin \n
    1 setlinecap \n

    /p0x 10 def \n
    /p0y 10 def \n
    /p1x 20 def \n
    /p1y 90 def \n
    /p2x 80 def \n
    /p2y 20 def \n
    /p3x 90 def \n
    /p3y 90 def \n

    /r 2 def \n

    newpath \n""")

f.write("""closepath \n

        gsave \n
        stroke\n
        showpage\n
        %EOF% xw\n""")
os.system("open " + shlex.quote(filename))