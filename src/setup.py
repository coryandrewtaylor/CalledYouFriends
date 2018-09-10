from setuptools import setup

setup(
    name='custom_tags',
    version='0.1',
    py_modules=['custom_tags'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        custom-tags=custom_tags:main
    ''',
)