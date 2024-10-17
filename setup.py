from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newlines and empty spaces
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='performanceppredict',
    version='0.0.1',
    author='Mayank',
    author_email='mayankpandey16122002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
