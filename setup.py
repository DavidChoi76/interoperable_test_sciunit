from setuptools import setup, find_packages
import os
from pip.__main__ import _main as main

error_log = open('error_log.txt', 'w')

def install(package):
    try:
        main(['install'] + [str(package)])
    except Exception as e:
        error_log.write(str(e))

if __name__ == '__main__':
    f = open('requirements.txt', 'r')
    for line in f:
        install(line)
    f.close()
    error_log.close()
    
setup(name='pyrhessys',
      description='A python wrapper for SUMMA',
      url='https://github.com/DavidChoi76/pyrhessys',
      author='YoungDon Choi',
      author_email='choiyd1115@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          ],
       extras_require={'plotting': [
          ],},
      include_package_data=True,
      test_suite='pyrhessys.tests')
