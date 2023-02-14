from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="faker_marketdata",
    version="0.3",
    author="Ruben Afonso",
    author_email="rbfrancos@gmail.com",
    description="Sample market data for Faker",
    long_description=long_description,
    long_description_content_type='text/markdown',
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
    install_requires=['Faker>=9.3.1', 'pycountry>=22.3.5']
)
