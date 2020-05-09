import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygames-stan", # Replace with your own username
    version="0.0.1",
    author="stan",
    author_email="tebigstan@riseup.net",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yorffuoj/pygames",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)