# setup.py

from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Plot Network using python , and output to DrawIO file'

with open('README.md') as readme_file:
       LONG_DESCRIPTION = readme_file.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="drawio_network_plot", 
        version="0.0.02Beta",
        author="Amr ElHusseiny",
        author_email="amroashram@hotmail.com",
        description=DESCRIPTION,
        long_description= LONG_DESCRIPTION ,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[], # No packages needed - all standard libraries
        keywords=['python', 'first package'],
        classifiers= ['Development Status :: 4 - Beta','Topic :: System :: Networking'],
        python_requires='>=3.6',
)