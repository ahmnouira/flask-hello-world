"""
Hello World app for running Python apps on Bluemix
"""

# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="flask-hello-world",
    version="1.0.0",
    description="Hello World app for running Python apps on Bluemix",
    long_description=long_description,
    url="https://github.com/AhmNouira/flask-hello-world",
    author="Ahmed Nouira",
    author_email="ahmnouira@gmail.com",
    license="MIT",
    keywords=["flask", "hello world"],
    install_requires=["flask", "gunicorn"],
    include_package_data=True,
    zip_safe=True,
    # entry_points="""[boot.sh]"""
)
