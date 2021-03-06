#!/usr/bin/env python

# This will try to import setuptools. If not here, it will reach for the embedded
# ez_setup (or the ez_setup package). If none, it fails with a message
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("lettucehoe could not be installed, probably because"
            " neither setuptools nor ez_setup are installed on this computer."
            "\nInstall ez_setup ([sudo] pip install ez_setup) and try again.")

from setuptools import setup, find_packages

setup(name='lettucehoe',
    version='0.1',
    author='kodda 2017',
    description='Segment crops and generate paths',
    long_description=open('README.rst').read(),
    url='http://github.com/p2pfoodlab/LettuceHoe',
    license='LGPL License',
    keywords="agriculture robotics weeding",
    packages= ['lettucehoe'],
    install_requires= ['numpy'])

