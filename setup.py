from setuptools import setup

setup(
    name='gulp',
    version='0.1.0',
    py_modules=['gulp'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'gulp = gulp:cli',
        ],
    }
)