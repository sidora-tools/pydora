# warinner-samples

Tools to retrieve samples metadata and informations from MPI-SHH internal database.


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
$ pip install git+ssh://git@gitlab.gwdg.de/paleobiotech/warinner-samples.git
```

## Example

```bash
$ warinner_samples credentials.json data/projects.txt data/tags.txt
Connected to Pandora Database
Retrieving samples and metadata
Samples and metadata have been written to /Users/borry/Documents/GWDG_Gitlab/warinner-samples/warinner_samples.csv
```

## Help


### Help menu 
```bash
$ warinner_samples --help
Usage: warinner_samples [OPTIONS] CREDENTIALS PROJECTS TAGS

  warinner_samples: retrieve samples metadata and informations from MPI-SHH internal database
  Author: Maxime Borry
  Contact: <borry[at]shh.mpg.de>
  Homepage: https://gitlab.gwdg.de/paleobiotech/warinner-samples

  CREDENTIALS: Json formatted files with credentials for accessing Pandora
  PROJECTS: File containing the list of projects to include (1 per line)
  TAGS: File containing the list of tags to include (1 per line)

Options:
  --version            Show the version and exit.
  --join [sql|pandas]  Join method  [default: sql]
  -o, --output PATH    Warinner samples metadata information  [default:
                       warinner_samples.csv]
  --help               Show this message and exit.
```

### Example input files

- An example [credentials.json](example_credentials.json) file
- An example [projects.txt](data/projects.txt) file
- An example [data/tags.txt](data/tags.txt) file

## Column list:

TBD when clearer deliverables.


## Pandora informations of interest to retrieve Warinner's group samples

### Projects:

- DAIRYCULTURES

- DAIRYCULTURES,Heirloom_Microbes

- Heirloom_Microbes

- Nepal_Upper_Mustang

- Oral_Microbiome_Evolution

- Origins of Dairying

- Richard III

### Tags

- Deep_Evolution

- Iberian_Transect

- Oral_Microbiome

- Richard_III

- Smoker calculus

- Modern dairy

- Nepal

- Pacific_calculus

- Unified_protocol

- Dental_arcade

- Modern_African_calculus

- James Fellows Yates

- Zandra Fagernäs

- Modern_African_calculus

- Irina_Velsko

- Tina Warinner

- Lena Semerau

#### Pandora SQL request

```sql
SELECT *
FROM `TAB_Raw_Data` rd

INNER JOIN `TAB_Sequencing` seq ON
rd.`Sequencing` = seq.`Id`

INNER JOIN `TAB_Capture` cap
ON seq.`Capture` = cap.Id

INNER JOIN `TAB_Library` lib
ON cap.`Library` = lib.`Id`

INNER JOIN `TAB_Protocol` AS lib_prot
ON lib.`Protocol` = lib_prot.`Id`

INNER JOIN `TAB_Extract` ext
ON lib.`Extract` = ext.`Id`

INNER JOIN `TAB_Sample` samp
ON ext.`Sample` = samp.`Id`

INNER JOIN `TAB_Protocol` AS ext_prot
ON ext.`Protocol` = ext_prot.`Id`

INNER JOIN (
	SELECT Id, Name as Sample_Type_Name 
	FROM `TAB_Type_Group`
) AS typ 
ON samp.`Type_Group` = typ.Id

INNER JOIN `TAB_Individual` ind
ON samp.`Individual` = ind.`Id`

INNER JOIN `TAB_Site` AS sit
 ON ind.`Site` = sit.`Id`
 
WHERE samp.`Projects` in (
 'DAIRYCULTURES',
 'DAIRYCULTURES,Heirloom_Microbes',
 'Heirloom_Microbes',
 'Nepal_Upper_Mustang',
 'Oral_Microbiome_Evolution',
 'Origins of Dairying',
 'Richard III')
 
OR samp.Tags REGEXP('Deep_Evolution|
 Iberian_Transect|
 James Fellows Yates|
 Oral_Microbiome|
 Dental_arcade|
 Zandra Fagernäs|
 Irina_Velsko|
 Modern_African_calculus|
 Tina Warinner|
 Richard_III|
 Lena Semerau|
 Smoker calculus|
 Modern dairy|
 Nepal|
 Pacific_calculus|
 Unified_protocol')
 
```