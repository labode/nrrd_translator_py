# Nrrd Translator
Tool to convert the labels in an Id labeled .nrrd graph to different labeling schemes.
Needs an existing id nrrd-file and a "dictionary" id/new label as .csv as input.
Optional (alternative) functionality: Label missing data points (segments missing in dictionary)

## Requirements
Required packages are listed in requirements.txt and can be installed using pip as follows:\
`pip3 install -r requirements.txt`

## Input
- .nrrd file with id labels
- .csv file containing id label value pairs
- Optional: Output filename (-o argument)
- Optional: Mode flag (-m argument)

## Output
- .nrrd containing the euler number

# Usage
`python3 nrrd_translator.py id.nrrd dictionary.csv -o outputfile.nrrd`
