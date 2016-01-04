from setuptools import setup
setup(
    name='pydagman',
    version='1.0',
    install_requires=['shortuuid'],
    packages=["pydagman"],
    url='https://github.com/brandentimm/pydagman',
    license='The MIT License (MIT)',
    author='brandentimm',
    author_email='branden.timm@gmail.com',
    description='Python library for creating DAGman job files for HTCondor'
)
