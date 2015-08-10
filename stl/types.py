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

import math


class Solid(object):
    """
    A solid object; the root element of an STL file.
    """

    #: The name given to the object by the STL file header.
    name = None

    #: :py:class:`list` of :py:class:`stl.Facet` objects representing the
    #: facets (triangles) that make up the exterior surface of this object.
    facets = []

    #: A scalar value (because STL files are unitless) that is the total
    #: surface area of the mesh. This is nothing more than a summation of
    #: the area of each facet
    surface_area = 0.0

    def __init__(self, name=None, facets=None, surface_area=None):
        self.name = name
        self.facets = facets if facets is not None else []

        if surface_area is not None:
            self.surface_area = self.calc_surface_area()
        else:
            self.surface_area = 0

    def add_facet(self, *args, **kwargs):
        """
        Append a new facet to the object and update
        :py:class:`stl.Solid.surface_area'. Takes the same arguments as the
        :py:class:`stl.Facet` type.
        """
        self.facets.append(Facet(*args, **kwargs))
        self._update_surface_area(self.facets[-1])

    def calc_surface_area(self):
        """
        Calculate the surface area of the :py:class:`stl.Solid` object
        """
        for facet in self.facets:
            self.surface_area += facet.area

    def _update_surface_area(self, facet):
        """
        Calculate the area of the given :py:class:`stl.Facet` and add it to the
        surface_area of the :py:class:`stl.Solid` object
        """
        self.surface_area += facet.area

    def write_binary(self, file):
        """
        Write this object to a file in STL *binary* format.

        ``file`` must be a file-like object (supporting a ``write`` method),
        to which the data will be written.
        """
        from stl.binary import write
        write(self, file)

    def write_ascii(self, file):
        """
        Write this object to a file in STL *ascii* format.

        ``file`` must be a file-like object (supporting a ``write`` method),
        to which the data will be written.
        """
        from stl.ascii import write
        write(self, file)

    def __eq__(self, other):
        if type(other) is Solid:
            if self.name != other.name:
                return False
            if len(self.facets) != len(other.facets):
                return False
            for i, self_facet in enumerate(self.facets):
                if self_facet != other.facets[i]:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<stl.types.Solid name=%r, facets=%r>' % (
            self.name,
            self.facets,
        )


class Facet(object):
    """
    A facet (triangle) from a :py:class:`stl.Solid`.
    """

    #: The uint16 of 'attribute bytes'. By the STL spec, these are unused and
    #: are generally supposed to both be \0. However, some modeling software
    #: uses them for various purposes.
    attributes = None

    #: The 'normal' vector of the facet, as a :py:class:`stl.Vector3d`.
    normal = None

    #: 3-element sequence of :py:class:`stl.Vector3d` representing the
    #: facet's three vertices, in order.
    vertices = None

    def __init__(self, normal, vertices, attributes=None):
        self.normal = Vector3d(*normal)
        self.vertices = tuple(
            Vector3d(*x) for x in vertices
        )

        if len(self.vertices) != 3:
            raise ValueError('Must pass exactly three vertices')

    def __eq__(self, other):
        if type(other) is Facet:
            return (
                self.normal == other.normal and
                self.vertices == other.vertices
            )
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<stl.types.Facet normal=%r, vertices=%r, area=%r>' % (
            self.normal,
            self.vertices,
            self.area,
        )

    @property
    def a(self):
        """
        The length the side of the facet between vertices[0] and vertices[1]
        """
        return abs(math.sqrt(pow((self.vertices[0].x - self.vertices[1].x), 2) +
                             pow((self.vertices[0].y - self.vertices[1].y), 2) +
                             pow((self.vertices[0].z - self.vertices[1].z), 2)))

    @property
    def b(self):
        """
        The length of the side of the facet between vertices[0] and vertices[2]
        """
        return abs(math.sqrt(pow((self.vertices[0].x - self.vertices[2].x), 2) +
                             pow((self.vertices[0].y - self.vertices[2].y), 2) +
                             pow((self.vertices[0].z - self.vertices[2].z), 2)))

    @property
    def c(self):
        """
        The length of the side of the facet between vertices[1] and vertices[2]
        """
        return abs(math.sqrt(pow((self.vertices[1].x - self.vertices[2].x), 2) +
                             pow((self.vertices[1].y - self.vertices[2].y), 2) +
                             pow((self.vertices[1].z - self.vertices[2].z), 2)))

    @property
    def perimeter(self):
        """
        The length of the perimeter of the facet
        """
        return self.a + self.b + self.c

    @property
    def area(self):
        """
        The surface area of the facet, as computed by Heron's Formula
        """
        p = self.perimeter / 2.0
        calced = abs(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
        return calced


class Vector3d(tuple):
    """
    Three-dimensional vector.

    Used to represent both normals and vertices of :py:class:`stl.Facet`
    objects.

    This is a subtype of :py:class:`tuple`, so can also be treated like a
    three-element tuple in (``x``, ``y``, ``z``) order.
    """

    def __new__(cls, x, y, z):
        return tuple.__new__(cls, (x, y, z))

    def __init__(self, x, y, z):
        pass

    @property
    def x(self):
        """
        The X value of the vector, which most applications interpret
        as the left-right axis.
        """
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        """
        The Y value of the vector, which most applications interpret
        as the in-out axis.
        """
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        """
        The Z value of the vector, which most applications interpret
        as the up-down axis.
        """
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value
