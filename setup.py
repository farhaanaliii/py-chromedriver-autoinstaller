# coding: utf-8
import os
import sys

from setuptools import setup

__author__ = "Farhan Ali <i.farhanali.dev@gmail.com>, Yeongbin Jo <iam.yeongbin.jo@gmail.com>"

with open("README.md") as readme_file:
    long_description = readme_file.read()

if sys.argv[-1] == "publish":
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
elif sys.argv[-1] == "clean":
    import shutil

    if os.path.isdir("build"):
        shutil.rmtree("build")
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    if os.path.isdir("py_chromedriver_autoinstaller.egg-info"):
        shutil.rmtree("py_chromedriver_autoinstaller.egg-info")

setup(
    name="py-chromedriver-autoinstaller",
    version="1.0.0",
    author="Farhan Ali",
    author_email="i.farhanali.dev@gmail.com",
    description="Automatically install chromedriver that supports the currently installed version of chrome.",
    license="MIT",
    keywords="chromedriver chrome chromium selenium",
    url="https://github.com/farhaanaliii/py-chromedriver-autoinstaller",
    packages=["py_chromedriver_autoinstaller"],
    install_requires=[
        'packaging>=23.1',
    ],
    entry_points={
        "console_scripts": [
            "chromedriver-path=py_chromedriver_autoinstaller.utils:print_chromedriver_path"
        ],
    },
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Installation/Setup",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)