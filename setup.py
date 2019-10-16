# Source: https://stackoverflow.com/questions/26900328/install-dependencies-from-setup-py
from pip._internal.req import parse_requirements

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