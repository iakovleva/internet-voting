import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        README = readme.read()

setup(
    name='internet-voting-system',
    version='0.1',
    packages=find_packages(),
    license='AGPL', 
    description='The prototype of fully end to end verifiable internet voting system.',
    long_description=README,
    url='https://github.com/python-dirbtuves/internet-voting',
    author='Python dirbtuves',
    author_email='python-dirbtuves@googlegroups.com',
    install_requires=[
        'cryptography',
    ],
    entry_points={
        'console_scripts': ['voter:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3'
    ],
)
