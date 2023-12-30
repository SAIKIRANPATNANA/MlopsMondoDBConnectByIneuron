import os
from pathlib import Path  
import logging

package_name = 'mongodb_connect'
list_of_files = [
    '.github/workflow/ci.yaml',
    '__init__.py',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/mongo_crud.py',
    'tests/__init__.py',
    'tests/unit/unit.py',
    'tests/integration/integration.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'experiments/emperiment.ipynb',
    'requirements.txt',
    'requirements_dev.txt',
    'tox.ini',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'init_setup.sh',
    '.gitignore'
]

for filepath in list_of_files:
    dir_name, file_name = os.path.split(filepath)
    if dir_name != '':
        os.makedirs(dir_name,exist_ok = True)
    if not os.path.exists(filepath) or not os.path.getsize(filepath):
        with open(filepath, 'w') as f:
            pass

