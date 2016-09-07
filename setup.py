import os
from setuptools import setup, find_packages

def requirements():
  """Build the requirements list for this project"""
  requirements_list = []
  with open('requirements.txt') as requirements:
    for install in requirements:
      requirements_list.append(install.strip())
  return requirements_list
setup(name='discord_simple',
  version='0.0.1.15',
  license='LGPLv3',
  description='Discord simple API',
  author='Alexander N. Skovpen',
  author_email='a.n.skovpen@gmail.com',
  url='https://github.com/askovpen/discord_simple/',
  install_requires=requirements(),
  packages=find_packages(exclude=['tests*']),
  include_package_data=True,
  extras_require={
    'json': 'ujson',
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
  ]
)
