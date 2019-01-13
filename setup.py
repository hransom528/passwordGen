from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()
setup(
    name="python-passwordgen",
    version="0.2",
    description="A useful password generator",
    liscense="GNU",
    author="Harris Ransom",
    author_email="hransom528@gmail.com",
    url="https://github.com/commanderHR1/python-password-generator",
    packages=["python-passwordgen"],
    install_requires=[],
)
