#!/usr/bin/env python3
'''
This file is part of python-stl, which is copyright 2015 Martin Atkins with
contributors listed the AUTHORS file and is licensed under the MIT License which
can be viewed at python-stl/LICENSE
'''

from stl import *

'''
NB: the datafile object is created using the 'rb' option flags, which ensures
that Python3's file.read method handles the data decoding correctly.
'''
datafile = open("/home/zwick/Readings/3D Printing/9mm_Magazine_Speed-Loader/9mm_speed_loader.STL",'rb')
parsed = stl.read_binary_file(datafile)

print("Name: " + str(parsed.name))
print("Facets: " + str(len(parsed.facets)))
print("Surface Area: " + str(parsed.surface_area))
