from setuptools import setup, find_packages

setup(name='pyrhessys',
      description='A python wrapper for RHESSys',
      url='https://github.com/UW-Hydro/pysumma.git',
      author='YoungDon Choi',
      author_email='choiyd1115@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          ],
       extras_require={'requirment': [
          'require.txt'
          ],},
      include_package_data=True)
