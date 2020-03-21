import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='my_project',
    packages=['my_project'],
    install_requires=install_requires
    )