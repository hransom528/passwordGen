import pathlib
from setuptools import setup

#The main directory
HERE = pathlib.Path(__file__).parent
#THe text of the README file
README = (HERE / "README.md").read_text()
with open("README.md", 'r') as f:
    long_description = f.read()


setup(
    name="python_password_generator",
    version="0.2",
    description="A useful password generator",
    author="Harris Ransom",
    author_email="hransom528@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    url="https://github.com/commanderHR1/python-password-generator",
    packages = ["python_password_generator"],
    include_package_data=True,
)
