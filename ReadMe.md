## xenaPythonTest
This is a [testpypi](https://testpypi.python.org/pypi) package for [xenaAPI](https://github.com/jingchunzhu/cgDataNew/tree/master/xena).
Also take a look at[#2](https://github.com/ucscXena/python-scripts/issues/2)

**UPDATE**: Published as [xenaPython](https://pypi.python.org/pypi/xenaPython). Find repo at [ucscXena/xenaPython](https://github.com/ucscXena/xenaPython).


---------
### Usage


The package can be installed as
 
    pip install -i https://testpypi.python.org/pypitest xenaPythonTest 

Use as 

    >>from xenaPythonTest import xenaAPI
    >>from xenaPythonTest import xenaQuery
 
 OR
 
    >>import xenaPythonTest as xena
    >>xena.xenaAPI                
    
    


### Packaging 


#### Installation 
    pip install twine
    
    
#### Run
    python setup.py sdist bdist_wheel           #build
    twine register -r pypitest dist/*           #register 
    twine upload -r pypitest dist/*             #upload 
