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

This file incorporates work covered by the following copyright and  
permission notice:  

Copyright (c) 2014, 2015 Martin Atkins <mart@degeneration.co.uk>  
Copyright (c) 2014, 2015 Stefan Blanke <greenarrow@users.sourceforge.net>
Copyright (c) 2014, 2015 dnkrtz <aidan.kurtz@mail.mcgill.ca>

Permission to use, copy, modify, and/or distribute this software  
for any purpose with or without fee is hereby granted, provided  
that the above copyright notice and this permission notice appear  
in all copies.  

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL  
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED  
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE  
AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR  
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS  
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,  
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN  
CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.  
'''

import struct
from stl.types import *


class Reader(object):

    def __init__(self, file):
        self.file = file
        self.offset = 0

    def read_bytes(self, byte_count):
        bytes = self.file.read(byte_count)
        if len(bytes) < byte_count:
            raise FormatError(
                "Unexpected end of file at offset %i" % (
                    self.offset + len(bytes),
                )
            )
        self.offset += byte_count
        return bytes

    def read_uint32(self):
        bytes = self.read_bytes(4)
        return struct.unpack('<I', bytes)[0]

    def read_uint16(self):
        bytes = self.read_bytes(2)
        return struct.unpack('<H', bytes)[0]

    def read_float(self):
        bytes = self.read_bytes(4)
        return struct.unpack('<f', bytes)[0]

    def read_vector3d(self):
        x = self.read_float()
        y = self.read_float()
        z = self.read_float()
        return Vector3d(x, y, z)

    def read_header(self):
        bytes = self.read_bytes(80)
        return bytes.decode().strip('\0')


class FormatError(ValueError):
    pass


def parse(file):
    r = Reader(file)

    name = r.read_header()

    ret = Solid(name=name)

    num_facets = r.read_uint32()

    for i in range(0, num_facets):
        normal = r.read_vector3d()
        vertices = tuple(
            r.read_vector3d() for j in range(0, 3)
        )

        attr_byte_count = r.read_uint16()
        if attr_byte_count > 0:
            # Some modeling software uses the attribute bytes for various
            # purposes, so don't skip attribute bytes
            attr_bytes = r.read_bytes(attr_byte_count)
        else:
            attr_bytes = None

        ret.add_facet(
            normal=normal,
            vertices=vertices,
            attributes=attr_bytes,
        )

    return ret


def write(solid, file):
    # Empty header
    file.write('\0' * 80)

    # Number of facets
    file.write(struct.pack('<I', len(solid.facets)))

    for facet in solid.facets:
        file.write(struct.pack('<3f', *facet.normal))
        for vertex in facet.vertices:
            file.write(struct.pack('<3f', *vertex))
        file.write('\0\0')  # no attribute bytes
