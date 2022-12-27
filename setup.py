from setuptools import setup, find_packages

setup(
    name="faker_finance",
    version="0.1",
    author="Ruben Afonso",
    author_email="rbfrancos@gmail.com",
    description="Sample financial data for Faker",
    url="https://github.com/rubenafo/faker_finance",
    keywords = ["faker", "testdata", "financedata", "python", "marketdata"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires='>=3.6',
)