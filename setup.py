from setuptools import setup, find_packages

setup(
    name="koyomi",
    version='1.0',
    description='Mutual conversion between the Japanese calendar and the Gregorian calendar',
    author='ken sugawara',
    author_email='anagomentai@gmail.com',
    url='https://github.com/nkrwgs/koyomi',
    packages=find_packages(),
    entry_points="""
	[console_scripts]
	wareki = wareki.cli:execute
    """,
)
