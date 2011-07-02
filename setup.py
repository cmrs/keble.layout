from setuptools import setup, find_packages
import os

version = open(os.path.join("oxford", "layout", "version.txt")).read().strip()

long_description = (
    read(os.path.join('docs', 'README.txt'))
    + '\n' +
    'Installing\n'
    '**************\n'
    + '\n' +
    read(os.path.join('docs', 'INSTALL.txt'))
    + '\n' +
    'History\n'
    '**********************\n'
    + '\n' +
    read(os.path.join('docs', 'HISTORY.txt'))
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read(os.path.join('docs', 'CONTRIBUTORS.txt'))
    + '\n' +
    'Download\n'
    '********\n')

setup(name='keble.layout',
      version=version,
      description="'The base layout for Keble sites'",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['keble'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
