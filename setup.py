from setuptools import setup, find_packages
from setuptools.command.install import install
import os


setup(
    name='tomolog',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Francesco De Carlo',
    author_email='decarlof@gmail.com',
    url='https://github.com/xray-imaging/tomolog',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/tomolog'],
    description='cli to create tomography experiment log documentation',
    zip_safe=False,
)