from setuptools import setup, find_packages
print(find_packages())
setup(
    name="xenaPythonTest",
    version="0.2.1",
    packages=find_packages(),
    author = 'GiriB',
    author_email = 'giri1gb@gmail.com',
    description = 'Test package for XENA API',
    url = 'https://github.com/jingchunzhu/cgDataNew/tree/master/xena', 
    keywords = ['xena', 'ucsc', 'xenaAPI'],
    license='MIT', 
    include_package_data=True, # To include files specified in MANIFEST.in
)
