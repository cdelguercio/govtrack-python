from setuptools import setup

setup(
  name='govtrack',
  packages=['govtrack'],
  install_requires=['unittest2==1.1.0','requests==2.9.1',],
  version='0.1',
  description='A Python library for the GovTrack.us API v2.',
  author='Chris Del Guercio',
  author_email='cdelguercio@gmail.com',
  url='https://github.com/cdelguercio/govtrack-python',
  download_url='https://github.com/cdelguercio/govtrack-python/tarball/0.1',
  keywords=['govtrack', 'api', 'python'],
  classifiers=[],
  test_suite='nose.collector',
  tests_require=['nose', 'nose-cover3'],
)
