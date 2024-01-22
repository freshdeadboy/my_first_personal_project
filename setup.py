from setuptools import setup, find_packages

setup(
    name='my_project_console',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'prettytable==2.2.1',
        'colorama==0.4.4',
    ],
    entry_points={
        'console_scripts': [
            'my_project_console = assistant.main:main',
        ],
    },
)