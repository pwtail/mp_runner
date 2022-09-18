
from setuptools import setup, find_packages

setup(name="multiunit",
      version="0.1.1",
      author="Vitalii Abetkin",
      author_email="abvit89s@gmail.ru",
      packages=find_packages(),
      description="Launch unittest in multiple processes",
      long_description="Launch unittest in multiple processes",
      license="MIT",
      classifiers=())


#TODO load_tests
#TODO allow to specify id
#TODO printing in proper order, messages

#TODO sqlite