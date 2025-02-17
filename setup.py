from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements required to run this project.
    :return: list of requirements
    """
    requirements = []
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements


setup(
    name='logs-classification',
    version='0.0.1',
    author='Tiyyagura Chandra Reddy',
    author_email='tchandrareddy21@gmail.com',
    url='https://github.com/tchandrareddy21/logs-classification',
    install_requires=get_requirements(),
    packages=find_packages()
)