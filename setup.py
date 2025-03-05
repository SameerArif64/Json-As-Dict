from setuptools import setup, find_packages

setup(
    name="json_as_dict",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Sameer Arif",
    author_email="supersameer64@gmail.com",
    description="A simple wrapper for JSON files to use them as Python dictionaries.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SameerArif64/json-as-dict",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)
