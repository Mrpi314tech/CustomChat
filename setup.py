from setuptools import setup, find_packages

setup(
    name='CustomChat',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
)
