import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S1FLAC2',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="# PiCKeT – SA’s Legal Fencing App\r\n\r\nOne of the most common issues that the Flinders Legal Centre (FLC) deals with is fencing disputes, and the process can be complicated because relevant legal issues must be considered before the correct advice can be given to clients. This takes up a significant amount of the FLC’s time and resources, therefore this app is designed to analyse clients’ initial inquiries and direct them to the appropriate resources. As the app can be accessed from anywhere, including on mobile devices, it will improve the clients’ experience because they can access relevant information that is tailored to their needs anywhere, and at any time.\r\n\r\n## Authors\r\nArjun Shivashankaraiah, Brayden Mann, Daniella De Vonte, Liam O'Shaughnessy, Lewis Suttie\r\n\r\n\r\n",
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S1FLAC2/', package='docassemble.LLAW33012021S1FLAC2'),
     )

