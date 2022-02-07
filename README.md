# PyDora

Toolkit to retrieve samples metadata and informations from MPI-EVA internal database. The Python cousin of [Sidora](https://github.com/sidora-tools/sidora.core)


## Install

- Install dependancies with conda

```bash
$ git clone git@gitlab.gwdg.de:paleobiotech/warinner-samples.git
$ cd warinner-samples
$ conda create -f environment.yml
$ conda activate paleobiotech
```

- Install using pip

```bash
$ pip install git+ssh://git@github.com/paleobiotechnology/pydora.git
```

## Example

```bash
$ pydora -c credentials.json -t assets/example_tags.txt
Successfully Connected to Pandora Database
Making request to Pandora SQL server
Downloaded table
Samples and metadata have been written to /Users/maxime/Documents/github/pydora/pandora_samples.csv
```

## Help


### Help menu 
```bash
$ pydora --help
Usage: pydora [OPTIONS]

  pydora: retrieve samples metadata and informations from MPI-SHH internal database
  Author: Maxime Borry
  Contact: <borry[at]shh.mpg.de>
  Homepage: https://gitlab.gwdg.de/paleobiotech/warinner-samples

  CREDENTIALS: Json formatted files with credentials for accessing Pandora
  PROJECTS: File containing the list of projects to include (1 per line)
  TAGS: File containing the list of tags to include (1 per line)

Options:
  --version               Show the version and exit.
  -c, --credentials PATH  [default: credentials.json]
  -p, --projects PATH     File listing projects to include (one per line)
  -t, --tags PATH         File listing tags to include (one per line)
  --join [sql|pandas]     Join method  [default: sql]
  -o, --output PATH       Warinner samples metadata information  [default:
                          pandora_samples.csv]
  --help                  Show this message and exit.
```

### Example input files

- An example [credentials.json](assets/example_credentials.json) file. For real credentials, please ask on the [Sidora mattermost channel](https://mattermost.eva.mpg.de/mpi-eva-dag/channels/sidora)
- An example [projects.txt](assets/example_projects.txt) file
- An example [tags.txt](assets/example_tags.txt) file


### Connecting through `shh` tunnel to Pandora

When connecting from outside the MPI-EVA servers (e.g.) from your laptop, through the VPN, you have to establish a shh tunnel

```bash
ssh -L 10001:pandora.eva.mpg.de:3306 <yourusername>@daghead1
```

You will need to slightly modify the credentials `json` file to account for the shh tunnel. An example `credentials.json` file when working through a ssh tunnel can be found here [assets/example_credentials_ssh_tunnel.json](assets/example_credentials_ssh_tunnel.json)

