from setuptools import setup, find_packages
print(find_packages())
setup(
    name="xenaPythonTest",
    version="0.2.1",
    packages=find_packages(),
    # I am not the author of the package. 
    # The author details are for testing purposes only.     
    author = 'GiriB',
    author_email = 'giri1gb@gmail.com',
    description = 'Test package for XENA API',
    url = 'https://github.com/jingchunzhu/cgDataNew/tree/master/xena', 
    keywords = ['xena', 'ucsc', 'xenaAPI'],
    license='MIT', 
)


# setup(
#   name = 'xenaPythonTest',
#   packages = ['xenaPythonTest'], # this must be the same as the name above
#   version = '0.1',
#   description = 'A random test lib',
#   maintainer = 'GiriB',
#   maintainer_email = 'giri1gb@gmail.com',
#   url = 'https://github.com/jingchunzhu/cgDataNew/tree/master/xena', 
#   keywords = ['xena', 'ucsc', 'xenaAPI'], 
# )
