# Nrrd Translator
Tool to convert the labels in an Id labeled .nrrd graph to different labeling schemes.
Needs an existing id nrrd-file and a "dictionary" id/new label as .csv as input.
Optional (alternative) functionality: Label missing data points (segments missing in dictionary)

# Usage
python nrrd_translator.py -i id.nrrd -c dictionary.csv -f outputfile