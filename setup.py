from setuptools import setup, find_packages
print(find_packages())
setup(
    name="xenaPythonTest",
    version="0.2.6",
    packages=find_packages(),
    # I am not the author of the package. 
    # The author details are for testing purposes only.     
    author = 'GiriB',
    author_email = 'giri1gb@gmail.com',
    description = 'Test package for XENA API',
    url = 'https://github.com/jingchunzhu/cgDataNew/tree/master/xena', 
    keywords = ['xena', 'ucsc', 'xenaAPI'],
    license='MIT', 
    include_package_data=True, # To include files specified in MANIFEST.in
)


