import os
import shutil

import setuptools

import pyarinc424

if not os.path.exists('pyarinc424'):
    os.mkdir('pyarinc424')
shutil.copyfile('pyarinc424.py', 'pyarinc424/__init__.py')

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'requests>=2.25.1',
    'pandas>=2.0.2',
    'click>=8.1.3'
]

setuptools.setup(
    name="pyarinc424",
    version=pyarinc424.__version__,
    author="Evgeny Varnavskiy",
    author_email="varnavruz@gmail.com",
    description="ARINC 424 parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varnav/pyarinc424",
    keywords=["arinc424", "arinc"],
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.9',
    entry_points={
        "console_scripts": [
            "pyarinc424 = pyarinc424:main",
        ]
    }
)
