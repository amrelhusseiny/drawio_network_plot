# setup.py

from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Plot Network using python , and output to DrawIO file'
LONG_DESCRIPTION = 'Plot Network using python , and output to DrawIO file'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="drawio_network_plot", 
        version="0.0.1",
        author="Jason Dsouza",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # No packages needed - all standard libraries
        keywords=['python', 'first package'],
        classifiers= ["No Classifier"],
        python_requires='>=3.6',
)