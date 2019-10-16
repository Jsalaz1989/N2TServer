from setuptools import find_packages, setup
# from pathlib import Path
# from typing import List

# # Source: https://www.it-swarm.net/es/python/requerimientos-de-referencia.txt-para-el-archivo-install-requires-kwarg-en-setuptools-setup.py/1071606334/
# def parse_requirements(filename: str) -> List[str]:
#     """Return requirements from requirements file."""
#     # Ref: https://stackoverflow.com/a/42033122/
#     # filePath = Path(__file__).parent/filename
#     # # print(f'{filePath}')

#     # text = filePath.read_text()
#     # print(f'{text}')

#     # text.replace(' ','')
#     # print(f'{text}')

#     # deps = text.split('\n')
#     # # print(f'{deps}')

#     with open('requirements.txt', 'rb') as reqFile:
#         lines = reqFile.readlines()
#         print(f'{lines}')

#     requirements = text.strip().split('\n')
#     requirements = [r.strip() for r in requirements]
#     requirements = [r for r in sorted(requirements) if r and not r.startswith('#')]
#     return requirements

# Source: https://stackoverflow.com/questions/26900328/install-dependencies-from-setup-py
from pip._internal.req import parse_requirements

# reqs = parse_requirements('requirements.txt')
# print('reqs = ', reqs)

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

reqs = load_requirements("requirements.txt")
print(f'{reqs}')

import sys
print(f'{sys.path}')

setup(
    name='n2tServer',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
)