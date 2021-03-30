from setuptools import setup, find_packages

setup(
    name = 'my_package',
    packages = find_packages(exclude=['tests*']),
    licence = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/<username>/<package-name>',
    author = '<Your Name>',
    author_email = '<Your Email>'
)