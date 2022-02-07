import pathlib
from pydora import __version__
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="pydora",
    version=__version__,
    description="Toolkot to retrive samples and metadata from MPI-EVA Pandora dabase",
    long_description=README,
    url="https://github.com/sidora-tools/pydora",
    long_description_content_type="text/markdown",
    license="GPLv3",
    python_requires=">=3.6",
    install_requires=[
        "pandas >=0.24.1",
        "sqlalchemy >= 1.3.13",
        "click >=7.0",
        "tqdm >=4.43.0",
    ],
    packages=find_packages(include=["pydora"]),
    entry_points={"console_scripts": ["pydora= pydora.cli:cli"]},
)
