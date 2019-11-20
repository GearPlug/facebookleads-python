import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='facebookmarketing-python',
      version='1.0.0',
      description='API wrapper for Facebook written in Python',
      url='https://github.com/GearPlug/facebookmarketing-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='MIT',
      packages=['facebookmarketing'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
