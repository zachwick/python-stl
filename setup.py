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

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="stl",
    version="dev",
    author="zach wick",
    author_email="zach@zachwick.com",
    description="Read and write STL 3D geometry files in both the ASCII and the binary flavor",

    packages=['stl'],
    install_requires=[
    ],
    setup_requires=[
        'nose>=1.0',
        'sphinx>=0.5',
    ],
    tests_require=[
        'nose>=1.0',
        'coverage',
        'mock',
        'pep8',
    ],
    test_suite='nose.collector',

    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],

    url='https://github.com/apparentlysmart/python-stl',
    license="MIT",
    keywords="stl 3d modelling geometry"
)
