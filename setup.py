from setuptools import setup, find_packages

setup(
    name='ipodget',
    version='0.1',
    url='https://github.com/dr1s/ipodget.py',
    author='dr1s',
    license='MIT',
    description='Copy all music from an iPod Video',
    install_requires=['eyed3'],
    packages=find_packages(),
    entry_points={'console_scripts': ['ipodget=ipodget.ipodget:main']},
)
