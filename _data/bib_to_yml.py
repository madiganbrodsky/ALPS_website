######
# bib_to_yml.py
# Stefan Pophristic
# Nov. 17, 2022
######
# Converts the bibtex file into a yaml file
#
# This script should be run everytime you wish to update the Publications section
# of the ALPS website
#
# Input: bib.bib which contains bibtex entries for all of the ALPS publications
# Output: bibliography.yml Yaml File which contains entries for all of the ALPS publications
#
# System requirements:
#  - Have python installed locally
#  - Have pyyaml installed locally
#       https://pyyaml.org/
#       install it by running 'pip install pyyaml' in terminal
#	- Have bibtexparser installed locally
#       https://bibtexparser.readthedocs.io/en/master/
#       install it by running 'pip install bibtexparser' in terminal
######

import yaml #pip install pyyaml
import bibtexparser #pip install bibtexparser

# open the bibtex file
with open('bib.bib') as bib:
    bib_data = bibtexparser.load(bib)

with open(r'bibliography.yml', 'w') as file:
    # Iterate through all entries
    # yaml.dump(bib_data, file) doesn't work because it'll include random bibtexparser
    #   code which will causes the liquid to not be able to parse the yaml file
    for bibEntry in bib_data.entries:
        # add the entry to the yaml file
        # bibEntry must be within [] in order to add it all to a single block
        #   (the "-" symbol that starts each entry in the yaml file)
        yaml.dump([bibEntry], file)
