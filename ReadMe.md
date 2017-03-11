##xenaPythonTest
This is testpypi package for [xenaAPI](https://github.com/jingchunzhu/cgDataNew/tree/master/xena) 

The package can be installed as
 
    pip install -i https://testpypi.python.org/pypitest xenaPythonTest 

Use as 

    >>from xenaPythonTest import xenaAPI
    >>from xenaPythonTest import xena_query
 
 OR
 
    >>import xenaPythonTest as xena
    >>xena.xenaAPI                
    


###Packaging 
####Installation 
    pip install twine
####Run
    python setup.py sdist bdist_wheel           #build
    twine register -r pypitest dist/*           #register 
    twine upload -r pypitest dist/*             #upload 
