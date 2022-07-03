from setuptools import setup, find_packages

setup(
	name='CropPricePrediction',
	version='1.0',
	author='Sai Prakash Davuluri',
	authour_email='saiprakashdavuluri@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
)