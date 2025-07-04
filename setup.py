from setuptools import setup, find_packages

setup(
    name="ez-chajim-intelli-chunk",
    version="5785.8.8",
    author="JEREMIA1964",
    author_email="bruder_joerg@hotmail.com",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=6.0",
        "PyGithub>=1.59",
    ],
    python_requires=">=3.8",
)
