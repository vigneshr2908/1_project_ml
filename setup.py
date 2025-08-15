from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

setup(
        name = 'mlproject',
        version = '0.0.1',
        author = 'Vignesh',
        author_email = 'vigneshr1711@gmail.com',
        packages = find_packages(),
        install_requires = get_requirements('requirements.txt')


)