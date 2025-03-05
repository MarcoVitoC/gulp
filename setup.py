from setuptools import setup, find_packages

setup(
    name='gulp',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'Click',
        'schedule',
        'plyer',
        'pyautostart'
    ],
    entry_points={
        'console_scripts': [
            'gulp = gulp:cli',
        ],
    }
)