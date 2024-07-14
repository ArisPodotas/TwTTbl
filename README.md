# Overview

TwTTbl Stand for Tree with a Taxonomic Table, this program uses a already made phylogenetic tree to add symbolism to the names automatically so that one does not need to parse the treefile on their own

## Preview

Tree before interpretations


Tree after interpretation


# Bootstrapping

This program parses the tree in a Nexus format and changes all the bootstrap values (assumes that the bootstrap has one NJ-bootstrap and one Bayesian/Likelyhood ratio value) to a format where all values less than 70 turn to "*". 

## Example

Value: 24.5/77 -> "*/ "
Value: 88/77 -> ""
Value: 24.5/18.8-> "*/*"
Value: 100/48.8-> " /*"
