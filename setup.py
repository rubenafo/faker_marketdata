from setuptools import setup, find_packages

setup(
    name="faker_marketdata",
    version="0.1",
    author="Ruben Afonso",
    author_email="rbfrancos@gmail.com",
    description="Sample market data for Faker",
    url="https://github.com/rubenafo/faker_marketdata",
    keywords = ["faker", "testdata", "financedata", "python", "marketdata", "isin", "sedol", "cusip",
                "ticker", "figi"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires='>=3.6',
)