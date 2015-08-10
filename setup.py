
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="stl",
    version="dev",
    author="Martin Atkins",
    author_email="mart@degeneration.co.uk",
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
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
    ],

    url='https://github.com/apparentlysmart/python-stl',
    license="MIT",
    keywords="stl 3d modelling geometry"
)
