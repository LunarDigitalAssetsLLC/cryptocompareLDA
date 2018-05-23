from setuptools import setup

with open('README.rst', encoding="utf-8") as f:
    readme = f.read()

setup(
        name='python_cryptocompare',
        version='0.0.1',
        description='Python Wrapper for CryptoCompare.com',
        long_description=readme,
        url='https://github.com/LunarDigitalAssetsLLC/python_cryptocompare',
        author='hanyoonLDA',
        author_email='han@lunardigitalassets.com',
        keywords='crypto cryptocurrency wrapper python api cryptocompare',
        license='MIT',
        python_requires='>=3',
        packages=['cryptocompare'],
        classifiers=['Programming Language :: Python :: 3'],
        install_requires=['requests']
        )
