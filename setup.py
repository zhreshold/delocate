#!/usr/bin/env python

from os.path import join as pjoin
from distutils.core import setup
import versioneer

versioneer.VCS = 'git'
versioneer.versionfile_source = pjoin('delocate', '_version.py')
versioneer.versionfile_build = pjoin('delocate', '_version.py')
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'delocate-'

setup(name='delocate',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Move OSX dynamic libraries into package',
      author='Matthew Brett',
      maintainer='Matthew Brett',
      author_email='matthew.brett@gmail.com',
      url='http://github.com/matthew-brett/delocate',
      packages=['delocate', 'delocate.tests'],
      package_data = {'delocate.tests':
                      [pjoin('data', '*.dylib'),
                       pjoin('data', 'test-lib'),
                       pjoin('data', 'make_libs.sh')]},
      license='BSD license'
     )
