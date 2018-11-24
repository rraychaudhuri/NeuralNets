# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='NeuralNet',
    version='1.0.0',
    description="Numpy based rusty implementation while reading Michael Nielsen's Deep Learning Book",
    long_description=readme,
    author='Rajat Raychaudhuri',
    author_email='rrc.999@gmail.com',
    url='https://github.com/rraychaudhuri/NeuralNets',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

