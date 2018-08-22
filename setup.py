# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='stock-quote-cli',
    version = '1.0.0',
    description= 'show stock info',
    author = 'yvvarun',
    author_email = 'yvvarun@gmail.com',
    url = 'https://github.com/yvvarun/stock-quote-cli',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stock = stock.stock_quote:main',
        ]
    },
)
