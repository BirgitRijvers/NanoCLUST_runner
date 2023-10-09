# NanoCLUST_runner
Python script that runs [NanoCLUST](https://github.com/genomicsITER/NanoCLUST) on files in a directory with only 1 command. 

## Introduction
With the [NC_runner.py](https://github.com/BirgitRijvers/NanoCLUST_runner/blob/main/NC_runner.py) script, you only have to enter a command once! 
The script starts a NanoCLUST run for files with a specified suffix in a directory you choose.

This script was developed because NanoCLUST often has to be used on multiple fastq files, but using wildcards to select multiple files doen't work optimally. 

## Usage
1. Download the [NC_runner.py](https://github.com/BirgitRijvers/NanoCLUST_runner/blob/main/NC_runner.py) script to a usefull location (preferably your home directory to avoid mistakes in the path)
2. Add the **absolute** paths for your database and taxdatabase to the argparse default part of the script (reduces the length of your commands and avoids mistakes in the paths)
3. Add the path to the main.nf file from NanoCLUST to the argparse default part of the script
4. *Optional*: Change the default output directory location to something usefull
5. *Optional*: Change the default suffix from the argparse part of the script to a suffix you will often use
6. Run the script!

If there is no input directory specified, or the input directory does not exist, the script will exit.

If the output direcotry does not exist, the script will notify you and create it.

## Output
The outputs of NanoCLUST will be placed in the output directory you specified, or in your current working directory (default).
For each NanoCLUST run, a separate folder will be created with the name of the corresponding sample.
Those folders contain the 3 output directories (classification data, fastqc results, pipeline info) created by NanoCLUST. 
## Example commands

*Basic command, only input directory specified (default settings):*
```bash
python NC_runner.py sequencedata 
```

*Input and output directory, file suffix specified*
```bash
python NC_runner.py sequencedata -o NanoCLUST_out -s .fastq.gz
```

*Input and output directory, file suffix, main.nf path specified*
```bash
python NC_runner.py sequencedata -o NanoCLUST_out -s .fastq.gz -n project1/programs/NanoCLUST/main.nf
```

*Input and output directory, file suffix, main.nf path, database paths specified*
```bash
python NC_runner.py sequencedata -o NanoCLUST_out -s .fastq.gz -n project1/programs/NanoCLUST/main.nf -d project1/db/16S_ribosomal_RNA -t project1/db/taxdb
```
