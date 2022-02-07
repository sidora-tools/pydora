[![Documentation Status](https://readthedocs.org/projects/pydora/badge/?version=latest)](https://pydora.readthedocs.io/en/latest/?badge=latest)

# PyDora

PyDora is a toolkit to retrieve samples an metadata and  from Pandora MPI-EVA internal database. PyDora is the Python cousin of [Sidora](https://github.com/sidora-tools/sidora.core).  

You can use PyDora both as a [command line tool](https://pydora.readthedocs.io/en/latest/CLI.html), or directly [from Python](https://pydora.readthedocs.io/en/latest/API.html).


## Installation

- Install using pip (most people)

  1. If you **don't** have set up your GitHub ssh keys

  ```bash
  $ pip install git+https://github.com/sidora-tools/pydora
  ```

  2. If you have set up your GitHub ssh keys

  ```bash
  $ pip install git+ssh://git@github.com/sidora-tools/pydora.git
  ```



- Install in dev environment

```bash
$ git clone git@github.com/sidora-tools/pydora.git
$ cd pydora
$ conda create -f environment.yml
$ conda activate pydora_dev
$ pip install -e .
```


## Quick start

```bash
$ pydora -c credentials.json -t assets/example_tags.txt
Successfully Connected to Pandora Database
Making request to Pandora SQL server
Downloaded table
Samples and metadata have been written to /Users/maxime/Documents/github/pydora/pandora_samples.csv
```

## Documentation

The documentation of PyDora is available here: [pydora.rtfd.io](http://pydora.readthedocs.io/)
