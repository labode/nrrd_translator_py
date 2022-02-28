# Nrrd Translator
Tool to convert the labels in an Id labeled .nrrd graph to different labeling schemes.
Needs an existing id nrrd-file and a "dictionary" id/new label as .csv as input.
Optional (alternative) functionality: Label missing data points (segments missing in dictionary)

## Requirements
Required packages are listed in requirements.txt and can be installed using pip as follows:\
`pip3 install -r requirements.txt`

# Usage
`python3 nrrd_translator.py -i id.nrrd -c dictionary.csv -f outputfile`
