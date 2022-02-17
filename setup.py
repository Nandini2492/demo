import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='demo',
    version='0.0.3',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Nandini2492/demo.git',
    packages=['demo'],
    install_requires=[],
)
