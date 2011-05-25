__author__="Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__ ="$20.05.2011 16:39:13$"

from setuptools import setup,find_packages

setup (
  name = 'Riso',
  version = '0.1-alpha2',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['threading', 'gtk', 'yaml', 'sqlalchemy'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'Robert Heumueller & Severin Orth',
  author_email = 'riso@ansha.eu',

  summary = 'Python Mud Client',
  url = '',
  license = '',
  long_description= 'An in Python + GTK written Mud Client',

  # could also include long_description, download_url, classifiers, etc.

  
)
