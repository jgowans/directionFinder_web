from setuptools import setup

setup(name='directionFinder_web',
      version = '0.0',
      description = 'Web interface to DF instrument',
      url= 'https://github.com/jgowans/directionFinder_web/',
      author = 'James Gowans',
      author_email = 'gowans.james@gmail.com',
      license = 'MIT',
      packages = ['directionFinder_web'],
      install_requires = [
          'directionFinder_backend',
          'pyramid',
      ],
      script = [
          'bin/run_directionFinder_web.py'
      ],
      zip_safe = False)
