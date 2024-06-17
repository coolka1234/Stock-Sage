from setuptools import setup, find_packages

setup(
    name='Stock_Sage',
    version='1.0.1',
    packages=find_packages(include=['database', 'database.*', 'gui', 'gui.*', 'src', 'src.*']),
    entry_points={
        'console_scripts': [
        ],
    },
    author='Krzysztof Kulka',
    author_email='krzysztof.kulka1234@gmail.com',
    description='Stock Sage is a tool for stock market analysis. It provides a variety of features for stock market analysis, including stock price prediction, sentiment analysis, and more.',
)