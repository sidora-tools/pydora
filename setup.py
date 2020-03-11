import pathlib
from warinner_samples import __version__
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='warinner_samples',
    version=__version__,
    description="Retrieving Warinner's group samples and metadata from MPI-SHH Pandora dabase",
    long_description=README,
    url='https://gitlab.gwdg.de/paleobiotech/warinner-samples',
    long_description_content_type="text/markdown",
    license='GPLv3',
    python_requires=">=3.6",
    install_requires=[
        'pandas >=0.24.1',
        'sqlalchemy >= 1.3.13',
        'plotnine >=0.6.0',
        'click >=7.0'
    ],
    packages=find_packages(include=['warinner_samples']),
    entry_points={
        'console_scripts': [
            'warinner_samples= warinner_samples.cli:cli'
        ]
    }
)