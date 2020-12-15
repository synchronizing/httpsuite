import setuptools

from httpsuite import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="httpsuite",
    version=__version__,
    author="Felipe Faria",
    description="Collection of tools to parse, manipulate, and compile raw HTTP messages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shades-sh/httpsuite",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
