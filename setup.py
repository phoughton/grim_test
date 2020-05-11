import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grim",
    version="0.1.3",
    author="Peter Houghton",
    author_email="pete@investigatingsoftware.co.uk",
    description="An implementation of the GRIM test, in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phoughton/grim_test",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)