from setuptools import find_packages,setup
from typing import List
 
def get_requirements(file_path)->List[str]:
    """
    this will return list of requirements

    """
    req_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements!='-e .':
                    req_list.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return req_list

setup(
    name="NetworkSecurities",
    version="0.0.1",
    author="Ramcharan",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

print(find_packages())