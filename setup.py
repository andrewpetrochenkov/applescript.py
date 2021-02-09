import setuptools

setuptools.setup(
    name='applescript',
    version='2021.2.9',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
