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

import stl.ascii
import stl.binary

from stl.types import Solid, Facet, Vector3d


def read_ascii_file(file):
    """
    Read an STL file in the *ASCII* format.

    Takes a :py:class:`file`-like object (supporting a ``read`` method)
    and returns a :py:class:`stl.Solid` object representing the data
    from the file.

    If the file is invalid in any way, raises
    :py:class:`stl.ascii.SyntaxError`.
    """
    return stl.ascii.parse(file)


def read_binary_file(file):
    """
    Read an STL file in the *binary* format.

    Takes a :py:class:`file`-like object (supporting a ``read`` method)
    and returns a :py:class:`stl.Solid` object representing the data
    from the file.

    If the file is invalid in any way, raises
    :py:class:`stl.binary.FormatError`.
    """
    return stl.binary.parse(file)


def read_ascii_string(data):
    """
    Read geometry from a :py:class:`str` containing data in the STL *ASCII*
    format.

    This is just a wrapper around :py:func:`read_ascii_file` that first wraps
    the provided string in a :py:class:`StringIO.StringIO` object.
    """
    from StringIO import StringIO
    return parse_ascii_file(StringIO(data))


def read_binary_string(data):
    """
    Read geometry from a :py:class:`str` containing data in the STL *binary*
    format.

    This is just a wrapper around :py:func:`read_binary_file` that first wraps
    the provided string in a :py:class:`StringIO.StringIO` object.
    """
    from StringIO import StringIO
    return parse_binary_file(StringIO(data))
