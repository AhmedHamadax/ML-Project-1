from setuptools import find_packages,setup
from typing import List

CONST_HYPEN='-e .'
def get_requirements(file_path:str)->List[str]:
    reqs=[]
    with open(file_path) as file:
        reqs=file.readlines()
        reqs=[r.replace("\n","") for r in reqs]
    if CONST_HYPEN in reqs:
        reqs.remove(CONST_HYPEN)
    return reqs


setup(
    name='mlproject',
    version='0.0.1',
    author='ahmed',
    author_email='ahmedhamada011001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)