from setuptools import setup, find_packages

setup(
    name='my_personal_assistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'prettytable',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'go_my_personal_assistant = my_personal_assistant.main:main',
        ],
    },
)
