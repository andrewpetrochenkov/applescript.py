import setuptools

setuptools.setup(
    name='applescript',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
