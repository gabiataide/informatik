from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="informatik",
    version="0.0.1",
    author="Gabriela de Ataide Magalhaes",
    author_email="gabiataide921@gmail.com",
    description="A package that gives you a weekly chore list",
    url="https://github.com/gabiataide/informatik",
    packages=['challenge']
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Mozilla Public License v2 (MPL-2.0)",
    ],
)
