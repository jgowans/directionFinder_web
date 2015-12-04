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
          'pyramid_chameleon',
          'pyramid_debugtoolbar',
          'waitress',
      ],
      scripts = [
          'bin/run_directionFinder_web.py'
      ],
      test_suite="directionFinder_web",
      zip_safe = False,
      entry_points="""\
      [paste.app_factory]
      main = directionFinder_web:main
      """
      )
