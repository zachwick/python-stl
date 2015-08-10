#!/usr/bin/env python3
'''
Copyright (c) 2015 zach wick <zach@zachwick.com>  

This file is free software: you may copy, redistribute and/or modify it  
under the terms of the GNU General Public License as published by the  
Free Software Foundation, either version 3 of the License, or (at your  
option) any later version.  

This file is distributed in the hope that it will be useful, but  
WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU  
General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program.  If not, see <http://www.gnu.org/licenses/>.  

'''

from stl import *

'''
NB: the datafile object is created using the 'rb' option flags, which ensures
that Python3's file.read method handles the data decoding correctly.
'''
datafile = open("./5mm_Calibration_Steps.stl",'rb')
parsed = stl.read_binary_file(datafile)

print("Name: " + str(parsed.name))
print("Facets: " + str(len(parsed.facets)))
print("Surface Area: " + str(parsed.surface_area))
