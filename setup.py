from distutils.core import setup

setup(
    name='PbPython',
    version='0.1.1',
    author='Michael Kunze',
    author_email='mikekunze@gmail.com',
    packages=['pb_py'],
    license='LICENSE.txt',
    url="http://github.com/pandorabots/pb-python",
    description='Code for making API calls to Pandorabots server.',
    install_requires=[
        "requests >= 2.1.1",
        ],
)
