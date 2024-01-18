from setuptools import setup, find_packages

setup(
    name='assistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'prettytable',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'assistant = assistant.main:main',
        ],
    },
)