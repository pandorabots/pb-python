from distutils.core import setup

setup(
    name='PbPython',
    version='0.1.6',
    author='Michael Kunze',
    author_email='michael.kunze@pandorabots.com',
    packages=['pb_py'],
    license='LICENSE.txt',
    url="https://developer.pandorabots.com/docs",
    description='Code for making API calls to Pandorabots server.',
    install_requires=[
        "requests >= 2.1.1",
        ],
)
