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
$ pip install git@gitlab.gwdg.de:paleobiotech/warinner-samples.git
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
  PROJECTS: List of projects to include
  TAGS: List of tags to include

Options:
  --version          Show the version and exit.
  -o, --output PATH  Warinner samples metadata information
                     [default: warinner_samples.csv]
```

### Example input files

- An example [credentials.json](example_credentials.json) file
- An example [projects.txt](data/projects.txt) file
- An example [data/tags.txt](data/tags.txt) file

## Column list:

- Analysis_Id
- Full_Analysis_Id
- Result_Directory
- Full_Raw_Data_Id
- Sequencing_Date
- Demultiplexed_Reads
- FastQ_Files
- Full_Sequencing_Id
- Run_Id
- Single_Stranded
- Weight_Lane_1-4
- Weight_Lane_1
- Weight_Lane_2
- Weight_Lane_3
- Weight_Lane_4
- Weight_Lane_5
- Weight_Lane_6
- Weight_Lane_7
- Weight_Lane_8
- Sequencing_Protocol
- Full_Capture_Id
- Full_Library_Id
- Quantification_pre-Indexing_total
- Quantification_post-Indexing_total
- Efficiency_Factor: Efficiency of indexing
- Library_Protocol
- Full_Extract_Id
- Full_Sample_Id
- Archaeological_ID
- Sampled_Quantity
- Ethically_culturally_sensitive: No reusing of these samples
- Tags
- Projects
- Extraction_protocol
- Sample_Type_Name
- Site
- Individual_Id
- Full_Individual_Id
- Owning_institution
- Contact_Person
- Provenience
- Organism
- Archaeological_ID.1
- C14_Uncalibrated: Mean C14 data
- C14_Uncalibrated_Variation: SD of C14_Uncalibrated
- C14_Calibrated_From: C14 calibrated date lower boundary
- C14_Calibrated_To: : C14 calibrated date upper boundary
- C14_Info
- C14_Id
- Notes_individual
- Site_Id
- Full_Site_Id
- Site_Name
- Locality
- Province
- Country
- Latitude
- Longitude
- Organism.1
- 3' C-to-T substitutions for 10 bases (%): Relates do aDNA damage
- 3' C-to-T substitutions for 10 bases (count): Relates do aDNA damage
- 3' G-to-A substitutions for 10 bases (%): Relates do aDNA damage
- 3' G-to-A substitutions for 10 bases (count): Relates do aDNA damage
- 5' C-to-T substitutions for 10 bases (%): Relates do aDNA damage
- 5' C-to-T substitutions for 10 bases (count): Relates do aDNA damage
- Average read/fragment length for at most 100,000 reads aligned to chr1
- Failed reads
- Failed reads (fwd+rev)
- Failed reads (fwd+rev) in %
- Failed reads in %
- Initial reads
- Initial reads (forward+reverse)
- Mapped fragments
- Mapped fragments (L>=30)
- Mapped fragments (L>=30) in %
- Mapped fragments in %
- Mapped reads (fwd+rev+merged)
- Mapped reads (fwd+rev+merged) in %
- Mapped reads/fragments
- Mapped reads/fragments (L>=30)
- Mapped reads/fragments (L>=30) in %
- Mapped reads/fragments in %
- Median read/fragment length for at most 100,000 reads aligned to chr1
- Merged reads
- Merged reads in %


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
FROM `TAB_Analysis_Result_String` ars
INNER JOIN `TAB_Analysis` an ON
 ars.`Analysis`= an.`Id`
 
INNER JOIN `TAB_Raw_Data` rd ON
an.`Raw_Data` = rd.`Id`

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
 
AND an.`Deleted` = 'false'
```