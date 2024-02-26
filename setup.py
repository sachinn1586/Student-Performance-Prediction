
from setuptools import find_packages, setup
from typing import List

# Defining a constant string representing '-e .' for later use
HYPEN_E_DOT = '-e .'

# Defining a function to retrieve requirements from a file
def get_requirements(file_path: str) -> List[str]:
    '''
    This function retrieves the list of requirements from a specified file.
    '''
    # Initialize an empty list to store requirements
    requirements = []
    # Open the specified file in read mode
    with open(file_path) as file_obj:
        # Read the lines from the file and store them in a list
        requirements = file_obj.readlines()
        # Removing newline characters from each requirement and updating the list
        requirements = [req.replace("\n", "") for req in requirements]
        # If '-e .' is present in the requirements list, remove it
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    # Return the list of requirements
    return requirements

#parameters for the Python package
setup(
    
    name='mlproject',
    version='0.0.1',
    author='Sachin Kumar',
    author_email='sachinkr1416@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
